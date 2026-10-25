#!/usr/bin/env python3
"""
openspec validate --strict — validación de consistencia de la capa SDD del
harness (principio §25). Solo usa la biblioteca estándar de Python 3.8+.

Uso (desde la raíz del proyecto):
    python openspec.py validate                  # errores bloquean, avisos informan
    python openspec.py validate --strict         # los avisos también bloquean (puerta P5)
    python openspec.py validate --strict --cambio C003
    python openspec.py validate --strict --cambio C003 --archivo   # pre-archivo (§26)
    python openspec.py validate --raiz ruta/al/proyecto

Código de salida: 0 = en verde, 1 = hay fallas, 2 = error de uso/estructura.

Nota: el nombre imita al CLI de OpenSpec (Fission-AI) a propósito, pero NO es
ese programa. Si algún día se instala el CLI real, este script se invoca como
`python openspec.py ...` y no hay conflicto.
"""
import argparse
import re
import sys
from pathlib import Path

VERIFICACIONES = {"automática", "automatica", "ejecución con evidencia",
                  "ejecucion con evidencia", "revisión de datos", "revision de datos"}
RE_REQ_HDR = re.compile(r"^#{3,4}\s+(~~)?([A-Z][A-Z0-9_]*-R\d+)\b")
RE_ESC_ID = re.compile(r"([A-Z][A-Z0-9_]*-R\d+\.S\d+)")
RE_CAMBIO_DIR = re.compile(r"^(C\d{3,})")
VACIOS = {"", "-", "—", "...", "<...>", "(se llena al implementar)"}


class Reporte:
    def __init__(self, estricto):
        self.estricto = estricto
        self.errores, self.avisos = [], []

    def error(self, donde, msg):
        self.errores.append(f"{donde}: {msg}")

    def aviso(self, donde, msg):
        self.avisos.append(f"{donde}: {msg}")

    def imprimir(self):
        for e in self.errores:
            print(f"  ✗ ERROR  {e}")
        for a in self.avisos:
            print(f"  {'✗' if self.estricto else '!'} AVISO  {a}")
        fallas = len(self.errores) + (len(self.avisos) if self.estricto else 0)
        modo = "--strict" if self.estricto else "normal"
        if fallas:
            print(f"\n✗ Validación ({modo}) FALLÓ: {len(self.errores)} errores, "
                  f"{len(self.avisos)} avisos.")
        else:
            print(f"\n✓ Validación ({modo}) en verde"
                  + (f" ({len(self.avisos)} avisos)." if self.avisos else "."))
        return 1 if fallas else 0


# ---------------------------------------------------------------- utilidades
def leer(p):
    return p.read_text(encoding="utf-8") if p.exists() else None


def vacio(celda):
    c = celda.strip()
    return c in VACIOS or (c.startswith("<") and c.endswith(">"))


def tablas(texto):
    """Devuelve lista de (encabezados, filas) de tablas markdown."""
    res, lineas, i = [], texto.splitlines(), 0
    while i < len(lineas):
        l = lineas[i].strip()
        if l.startswith("|") and i + 1 < len(lineas) and re.match(r"^\|\s*:?-{2,}", lineas[i + 1].strip()):
            enc = [c.strip().lower() for c in l.strip("|").split("|")]
            filas, i = [], i + 2
            while i < len(lineas) and lineas[i].strip().startswith("|"):
                filas.append([c.strip() for c in lineas[i].strip().strip("|").split("|")])
                i += 1
            res.append((enc, filas))
        else:
            i += 1
    return res


def col(enc, *nombres):
    for n in nombres:
        for idx, h in enumerate(enc):
            if h.startswith(n):
                return idx
    return None


def secciones(texto, nivel):
    """Divide por encabezados de un nivel exacto: {titulo: cuerpo}."""
    patron = re.compile(rf"^{'#' * nivel}\s+(.+)$", re.M)
    marcas = list(patron.finditer(texto))
    out = {}
    for k, m in enumerate(marcas):
        fin = marcas[k + 1].start() if k + 1 < len(marcas) else len(texto)
        out[m.group(1).strip()] = texto[m.end():fin]
    return out


def requisitos_y_escenarios(texto):
    """Mapa req -> lista de filas de escenario (dict) dentro del texto dado."""
    reqs, actual, eliminados = {}, None, set()
    bloques = re.split(r"(?m)^(#{3,4}\s+.*)$", texto)
    for b in bloques:
        m = RE_REQ_HDR.match(b.strip()) if b.strip().startswith("#") else None
        if m:
            actual = m.group(2)
            reqs.setdefault(actual, [])
            if m.group(1) or "⛔" in b:
                eliminados.add(actual)
            continue
        if b.strip().startswith("#"):
            actual = None
            continue
        if actual is None:
            continue
        for enc, filas in tablas(b):
            ci = col(enc, "escenario")
            if ci is None:
                continue
            idx = {k: col(enc, k) for k in ("dado", "cuando", "entonces", "verificación", "verificacion", "verificado")}
            for f in filas:
                ids = RE_ESC_ID.findall(f[ci]) if ci < len(f) else []
                g = lambda k: f[idx[k]] if idx[k] is not None and idx[k] < len(f) else ""
                reqs[actual].append({
                    "id": ids[0] if ids else f[ci],
                    "dado": g("dado"), "cuando": g("cuando"), "entonces": g("entonces"),
                    "verif": g("verificación") or g("verificacion"),
                    "por": g("verificado"),
                })
    return reqs, eliminados


# ---------------------------------------------------------------- chequeos
def validar_escenarios(rep, donde, reqs, exigir_verificado):
    vistos = set()
    for req, escs in reqs.items():
        if not escs:
            rep.error(donde, f"{req} no tiene escenarios (§22).")
        for e in escs:
            eid = e["id"]
            if not RE_ESC_ID.fullmatch(eid):
                rep.error(donde, f"escenario sin ID válido '{eid}' en {req}.")
                continue
            if not eid.startswith(req + "."):
                rep.error(donde, f"{eid} está bajo {req}: el prefijo no coincide.")
            if eid in vistos:
                rep.error(donde, f"{eid} duplicado (los IDs no se reciclan).")
            vistos.add(eid)
            for campo in ("dado", "cuando", "entonces"):
                if vacio(e[campo]):
                    rep.error(donde, f"{eid} sin {campo.upper()} observable.")
            if e["verif"].strip().lower() not in VERIFICACIONES:
                rep.error(donde, f"{eid} con tipo de verificación inválido '{e['verif']}' "
                                 "(Automática / Ejecución con evidencia / Revisión de datos).")
            if exigir_verificado:
                if vacio(e["por"]):
                    rep.error(donde, f"{eid} sin «Verificado por» (no está terminado).")
                elif "✅" not in e["por"]:
                    rep.aviso(donde, f"{eid}: «Verificado por» sin ✅ (¿prueba en verde?).")
    return vistos


def cargar_specs(rep, raiz):
    dspecs = raiz / "specs"
    if not dspecs.is_dir():
        rep.error("estructura", "falta la carpeta specs/ (capa SDD obligatoria).")
        return {}, set(), set()
    todos, elim, escs = {}, set(), set()
    for p in sorted(dspecs.glob("*.md")):
        texto = leer(p)
        donde = f"specs/{p.name}"
        if "## Propósito" not in texto and "## Proposito" not in texto:
            rep.aviso(donde, "sin sección «## Propósito».")
        reqs, e = requisitos_y_escenarios(texto)
        vivos = {r: v for r, v in reqs.items() if r not in e}
        for r in reqs:
            if r in todos:
                rep.error(donde, f"{r} ya existe en otra spec (ID duplicado).")
        todos.update(reqs)
        elim |= e
        escs |= validar_escenarios(rep, donde, vivos, exigir_verificado=True)
    return todos, elim, escs


def validar_cambio(rep, raiz, dcambio, specs_reqs, specs_elim, planner, archivo):
    cid = RE_CAMBIO_DIR.match(dcambio.name).group(1)
    base = f"cambios/{dcambio.name}"
    prop = leer(dcambio / "propuesta.md")
    if prop is None:
        rep.error(base, "falta propuesta.md (puerta P1).")
        return
    expres = bool(re.search(r"\*\*Tipo:\*\*\s*exprés|\*\*Tipo:\*\*\s*expres", prop, re.I))
    if not re.search(r"-\s*\[x\]\s*Aprobada", prop, re.I):
        rep.error(f"{base}/propuesta.md", "propuesta sin aprobación marcada (P1 🔒).")
    for sec in ("## Por qué", "## Qué cambia", "## Fuera de alcance"):
        if sec not in prop:
            rep.error(f"{base}/propuesta.md", f"falta sección «{sec}».")
    if expres:
        if (dcambio / "delta.md").exists():
            rep.aviso(base, "cambio exprés con delta.md: ¿cambia comportamiento? Entonces no es exprés.")
        return

    # capacidades declaradas en la propuesta
    caps = set()
    for enc, filas in tablas(prop):
        ci = col(enc, "capacidad")
        if ci is not None:
            for f in filas:
                m = re.search(r"`?([A-Z][A-Z0-9_]*)`?", f[ci])
                if m:
                    caps.add(m.group(1))
    if not caps:
        rep.error(f"{base}/propuesta.md", "sin tabla «Capacidades afectadas».")

    # diseño
    dis = leer(dcambio / "diseno.md")
    if dis is None:
        rep.error(base, "falta diseno.md (puerta P2).")
    else:
        d = f"{base}/diseno.md"
        if "antes / después" not in dis.lower() and "antes/después" not in dis.lower():
            rep.error(d, "falta la tabla de comportamiento antes/después (§23).")
        if "mapeo" not in dis.lower():
            rep.error(d, "falta la sección de mapeo explícito (§23).")
        for enc, filas in tablas(dis):
            if col(enc, "supuesto") is not None:
                ce = col(enc, "estado")
                for f in filas:
                    est = f[ce] if ce is not None and ce < len(f) else ""
                    sid = f[0]
                    if "⬜" in est or vacio(est):
                        rep.error(d, f"supuesto {sid} sin verificar (puerta P3).")
                    elif "❌" in est:
                        rep.aviso(d, f"supuesto {sid} resultó falso: ¿quedó en learn.md y se ajustó el diseño?")
            if col(enc, "pregunta") is not None:
                cd = col(enc, "disposición", "disposicion")
                for f in filas:
                    disp = f[cd] if cd is not None and cd < len(f) else ""
                    plantilla = all(k in disp.lower() for k in ("resuelta", "fuera de alcance", "riesgo aceptado"))
                    if vacio(disp) or plantilla:
                        rep.error(d, f"pregunta {f[0]} sin disposición (puerta P4 🔒).")

    # delta
    delta = leer(dcambio / "delta.md")
    if delta is None:
        rep.error(base, "falta delta.md (puerta P2).")
        return
    dd = f"{base}/delta.md"
    secs_cap = {t.strip("` "): c for t, c in secciones(delta, 2).items()
                if re.fullmatch(r"`?[A-Z][A-Z0-9_]*`?", t.strip())}
    for c in caps - set(secs_cap):
        rep.error(dd, f"la propuesta declara {c} pero el delta no tiene «## {c}».")
    for c in set(secs_cap) - caps:
        rep.aviso(dd, f"el delta toca {c}, que no está en la propuesta.")

    esc_delta = set()
    for cap, cuerpo in secs_cap.items():
        ops = secciones(cuerpo, 3)
        for op, txt in ops.items():
            opn = op.upper().replace("Ó", "O")
            reqs, _ = requisitos_y_escenarios(txt)
            for r in reqs:
                if not r.startswith(cap + "-"):
                    rep.error(dd, f"{r} está en la sección {cap}.")
            if opn.startswith("AGREGADO"):
                for r in reqs:
                    if r in specs_reqs or r in specs_elim:
                        rep.error(dd, f"{r} AGREGADO pero ese ID ya existe en specs/ (no reciclar).")
                esc_delta |= validar_escenarios(rep, dd, reqs, exigir_verificado=archivo)
            elif opn.startswith("MODIFICADO"):
                for r in reqs:
                    if r not in specs_reqs:
                        rep.error(dd, f"{r} MODIFICADO pero no existe en specs/.")
                    if "**Antes:**" not in txt or "**Después:**" not in txt:
                        rep.error(dd, f"{r} MODIFICADO sin «Antes/Después».")
                con_esc = {r: v for r, v in reqs.items() if v}
                for r, v in reqs.items():
                    if not v:
                        rep.aviso(dd, f"{r} MODIFICADO sin escenarios nuevos/modificados: ¿siguen valiendo los actuales?")
                esc_delta |= validar_escenarios(rep, dd, con_esc, exigir_verificado=archivo)
            elif opn.startswith("ELIMINADO"):
                for r in reqs:
                    if r not in specs_reqs:
                        rep.error(dd, f"{r} ELIMINADO pero no existe en specs/.")
                    if "**Motivo:**" not in txt:
                        rep.error(dd, f"{r} ELIMINADO sin motivo.")
    if not esc_delta and not any(secciones(c, 3).keys() for c in secs_cap.values()):
        rep.error(dd, "delta vacío: si no cambia comportamiento, márcalo como cambio exprés.")

    # cobertura en planner
    if planner is None:
        rep.error("planner.md", "no existe; las tareas viven allí (§15).")
    else:
        if cid not in planner:
            rep.error("planner.md", f"no hay tareas del cambio {cid}.")
        for e in sorted(esc_delta):
            if e not in planner and not re.search(re.escape(e.rsplit(".S", 1)[0]) + r"\.S\d+[^|]*\.S", planner) \
                    and not _cubierto_corto(planner, e):
                rep.error("planner.md", f"{e} ({cid}) no está asignado a ninguna tarea.")


def _cubierto_corto(planner, eid):
    """Acepta notación abreviada en planner: '`CAP-R1.S1`, `.S2`'."""
    req, s = eid.rsplit(".", 1)
    for linea in planner.splitlines():
        if req in linea and re.search(rf"(?<![\w-])\.{s}\b", linea):
            return True
    return False


def validar_sensibles(rep, raiz):
    for nombre in ("local_privado",):
        if (raiz / nombre).exists():
            gi = leer(raiz / ".gitignore") or ""
            if nombre not in gi:
                rep.error(".gitignore", f"existe {nombre}/ pero no está ignorada (§17). "
                                        "Verifica con `git check-ignore -v`.")


def main():
    ap = argparse.ArgumentParser(prog="openspec", description="Validación SDD del harness")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate", help="valida specs/ y cambios/ activos")
    v.add_argument("--strict", action="store_true", help="los avisos también fallan")
    v.add_argument("--cambio", help="valida solo este cambio (p. ej. C003)")
    v.add_argument("--archivo", action="store_true",
                   help="chequeo pre-archivo: exige «Verificado por» en el delta (§26)")
    v.add_argument("--raiz", default=".", help="raíz del proyecto (por defecto, la actual)")
    a = ap.parse_args()

    raiz = Path(a.raiz).resolve()
    rep = Reporte(a.strict)
    print(f"openspec validate {'--strict ' if a.strict else ''}— {raiz}\n")

    specs_reqs, specs_elim, _ = cargar_specs(rep, raiz)
    dcambios = raiz / "cambios"
    if not dcambios.is_dir():
        rep.error("estructura", "falta la carpeta cambios/.")
    else:
        planner = leer(raiz / "planner.md")
        activos = [d for d in sorted(dcambios.iterdir())
                   if d.is_dir() and d.name != "archivo" and RE_CAMBIO_DIR.match(d.name)]
        if a.cambio:
            activos = [d for d in activos if d.name.startswith(a.cambio)]
            if not activos:
                print(f"No existe un cambio activo {a.cambio} en cambios/.")
                return 2
        for d in activos:
            validar_cambio(rep, raiz, d, specs_reqs, specs_elim, planner, a.archivo)
        for d in sorted(dcambios.iterdir()):
            if d.is_dir() and d.name != "archivo" and not RE_CAMBIO_DIR.match(d.name):
                rep.aviso("cambios/", f"carpeta '{d.name}' no sigue la convención Cnnn-<verbo-objeto>.")
    validar_sensibles(rep, raiz)
    return rep.imprimir()


if __name__ == "__main__":
    sys.exit(main())
