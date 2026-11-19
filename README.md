# Django generátor blbostí

Jednoduchá webovka v Django. Po každém kliknutí Python vybere jinou náhodnou hlášku.
Funguje lokálně na Windows a lze ji nasadit z GitHubu na Render.

## 1. Spuštění na Windows (PowerShell)

V rozbalené složce projektu otevři terminál (např. přes VS Code → Terminal → New Terminal).
Měj nainstalovaný Python, alespoň 3.10.

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py runserver
```

Otevři **http://127.0.0.1:8000/**.
Server ukončíš klávesami **Ctrl+C**.

### Testy

```powershell
.\.venv\Scripts\python.exe manage.py test
```

## 2. Push na GitHub

Na https://github.com/new vytvoř repozitář (např. `django-generator-blbosti`), ale
**nezatrhávej** přidání README ani .gitignore (už je máme).

V terminálu v kořenové složce projektu:

```powershell
git init
git add .
git commit -m "První verze Django webu"
git branch -M main
git remote add origin https://github.com/TVUJ-UCET/django-generator-blbosti.git
git push -u origin main
```

`TVUJ-UCET` nahraď přihlašovacím jménem na GitHubu. Pokud Git nezná tvoji identitu,
nastav `git config --global user.name "Jméno"` a
`git config --global user.email "tvuj@email.cz"`.

Při další změně stačí:

```powershell
git add .
git commit -m "Uprava webu"
git push
```

## 3. Hosting Render (Free)

1. Přihlas se na https://dashboard.render.com/.
2. Klikni **New → Web Service**, připoj GitHub a zvol svůj repozitář.
3. Nastav **Language: Python 3** a **Instance type: Free**.
4. **Build Command**:

   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput
   ```

5. **Start Command**:

   ```bash
   gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
   ```

6. V části **Environment** přidej `DJANGO_SECRET_KEY` a nech si vygenerovat dlouhou tajnou hodnotu.
7. Vytvoř službu. Render si kód stáhne z GitHubu. Výsledná adresa bude `https://neco.onrender.com/`.
8. Zapni automatické nasazení po commitu (**Auto-Deploy**, pokud není již zapnuté).

**Poznámka:** Tento projekt nepotřebuje databázi. Render Free se po nečinnosti uspává,
první načtení stránky může trvat déle. Není to produkční hosting.

## Co je kde

- `manage.py` – ovládání Django projektu, spuštění lokálního serveru.
- `config/settings.py` – nastavení (hosty, statické soubory, tajný klíč).
- `config/urls.py` – propojení URL na aplikaci.
- `generator/views.py` – Python kód, který losuje hlášky.
- `generator/urls.py` – adresy `/` a `/health/`.
- `generator/templates/generator/index.html` – HTML šablona.
- `generator/static/generator/style.css` – vzhled stránky.
- `generator/tests.py` – jednoduché testy.

## Když něco nefunguje

- `py není rozpoznán` → nainstaluj Python z python.org a zaškrtni přidání do PATH.
- `git není rozpoznán` → nainstaluj Git z git-scm.com.
- `DisallowedHost` na Renderu → zkontroluj, zda Render nastavil `RENDER_EXTERNAL_HOSTNAME`.
- `DJANGO_SECRET_KEY` chybí → přidej proměnnou do Environment v Renderu.
- Statické soubory na Renderu chybí → ověř, že Build Command obsahuje `collectstatic`.

## Stav a zdraví

- `GET /` – hlavní webovka s hláškou.
- `GET /health/` – jednoduchá odpověď `{"status": "ok"}`.
