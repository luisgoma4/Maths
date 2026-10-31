# Seguridad: revisión del 2026-10-31

Contexto: revisión de seguridad de todos los repos tras el «octubre negro» (la IA abarata el ataque: se asume que todo repo, endpoint y clave se escanea en minutos). Este documento recoge lo aplicado a este repo y lo que queda pendiente; el estado vive en `docs/`, no en la conversación.

> Repo **público**: los pendientes se describen por categoría y acción, sin detalles explotables.

## Cambios aplicados

Ninguno en esta tanda.

## Pendientes

- [ ] **Info** · Metadatos de commit (E-03): Email `noreply` de GitHub en commits futuros; no reescribir el historial ya indexado.
- [ ] **Info** · Repo (E-29, E-66): Activar Secret scanning + Push protection y añadir `SECURITY.md` mínimo.

## Reglas nuevas para agentes de este repo

- En repos públicos, commits con el email `noreply` de GitHub.
- .gitignore base: `.env*`, `*.pem`, `*.key`, `*.sqlite*`, `*.db`, `.wrangler/`, y `*.xlsx`/`*.docx`/`*.pdf` en repos con material de cliente. Ejecutar `gitleaks detect --log-opts=--all` antes de hacer público un repo.
- Antes de añadir dependencias o CI, lockfile y Actions por SHA.
