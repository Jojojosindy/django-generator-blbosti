"""Serverová logika: Django náhodně vybere jednu větu."""
import random
from django.http import JsonResponse
from django.shortcuts import render

HLASKY = [
    "Když se ti nedaří, zkus změnit font.",
    "Pokud tě honí čas, zkus běžet rychleji než hodiny.",
    "Včerejší problém je dnešní historický dokument.",
    "Jestli nevíš, kudy dál, nejdřív zjisti, kde je dál.",
    "Máš-li hlad po úspěchu, nejdřív otevři ledničku.",
    "Některé dveře se otevřou jen tehdy, když mají kliku.",
    "Neodkládej na zítřek, co můžeš odložit na příští týden.",
    "Život je jako Wi-Fi. Někdy máš plný signál a nic nefunguje.",
    "Pokud plán A nevyšel, abeceda má ještě spoustu písmen.",
    "Každá chyba je příležitost vytvořit novou chybu.",
    "Když se ztratíš, tvůj nový cíl je místo, kde právě stojíš.",
    "I špatný nápad může být výborně zdokumentovaný.",
    "Nikdy nevěř kalkulačce, která tvrdí, že má city.",
    "Čím rychleji stojíš, tím méně se pohybuješ.",
    "Zázraky se dějí, ale většinou nemají dokumentaci.",
]


def home(request):
    # Ať se po kliknutí nevrátí hned stejná hláška.
    previous = request.GET.get("previous", "")
    choices = list(range(len(HLASKY)))
    if previous.isdigit() and int(previous) in choices and len(choices) > 1:
        choices.remove(int(previous))
    selected = random.choice(choices)
    return render(request, "generator/index.html", {
        "hlaska": HLASKY[selected],
        "selected": selected,
        "total": len(HLASKY),
    })


def health(request):
    return JsonResponse({"status": "ok"})
