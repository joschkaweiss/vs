from flask import Flask
import random

app = Flask(__name__)

def menu():
    return """
            <br>
            <a href="/1"> Kapitel 1 </a>
            <br>
            <a href="/2"> Kapitel 2 </a>
            <br>
            <a href="/3"> Kapitel 3 </a>
            <br>
            <a href="/4"> Kapitel 4 </a>
            """


def antwort(frage, arr, x):
    return """
            <button onclick="myFunction()">Zeige Antwort</button>

            <div id="myDIV" style="display: none">""" + arr[frage].get_antwort() + """
                
            </div>
            <br>
            <br>
            <br>
            <a href=/""" + str(x) + """> <button> Nächste Frage </button> </a>
            <br>
            <br>
            """



def addScript():
    return """
    <script>
    function myFunction() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
    </script> 
    """

class Frage:
    def __init__(self, frage, aw):
        self.frage = "<h4>" + frage + "</h4>"
        self.antwort = "<p>" + aw + "</p>"
        self.wert = 0

    def get_wert(self):
        return self.wert

    def get_frage(self):
        return self.frage

    def get_antwort(self):
        return self.antwort

    def plus_wert(self):
        self.wert += 1

    def minus_wert(self):
        self.wert -= 1


kap1 = [Frage("In welcher Situation ist es unmöglich den Zustand vor einer abgebrochenen Transaktion wiederherzustellen?", "Jeder Zustand, in dem E/A Operationen durchgeführt wurden, kann nicht rückgängig gemacht werden"),
        Frage("Beschreiben Sie genau, was ein skalierbares System ist.", "Skalierungsdimensionen: <br> -Anzahl an Komponenten<br> -geografische Größe<br> -Anzahl und Größe der administrativen Domänen<br> System ist skalierbar, wenn es in einer oder mehreren dieser Dimensionen ohne einen signifikanten Performanzverlust wachsen kann."),
        Frage("Für die Ausführung verschachtelter Transaktionen ist eine Form der Koordination nötig. Erklären Sie, was ein Koordinator leisten sollte.", "Koordinator muss sicherstellen, dass ein Commit erfolgt, sobald alle Transaktionen dazu bereit sind und dass der Abbruch einer verschachtelten Transaktion zum Abbruch aller untergeordneten Transaktionen führt."),
        Frage("Nicht immer sind alle Arten der Transparenz in pervasiven Systemen angebracht. Nennen Sie jeweils ein Beispiel, wo Transparenz wünschenswert bzw. nicht wünschenswert ist.", "Wünschenswert: Migrationstransparenz <br> Nicht wünschenswert: Ortstransparenz"),
        Frage("In der Vorlesung wurden bereits einige Beispiele für verteilte pervasive Systeme genannt: Haussysteme, elektronische Systeme im Gesundheitswesen und Sensornetze. Erweitern Sie diese Aufstellung um weitere Beispiele.", "Systeme zur Umwelt und Klimaüberwachung. <br> elektrische Fußfesseln <br> Systeme im Bereich Sport und Medizin zur Überwachung verurteilter Straftäter.")
        ]

kap2 = [Frage("Wenn ein Client und ein Server weit voneinander entfernt aufgestellt werden, sehen wir möglicherweise, dass die Latenzzeit des Netzwerkes die Gesamtleistung bestimmt. Wie können wir dieses Problem angehen?", "Lösungsmöglichkeiten hängen davon ab, wie Client organisiert ist  ein möglicher Ansatz: zeitliche Aufteilung der Kommunikation <br>- Client teilt Code in kleinere Teile auf <br>- während eine Anfrage abgearbeitet und auf den Server gewartet wird, wird ein anderer Client-Codeteil weitergearbeitet <br>- durch die frühere Anfrage des Servers nach einem Teil der Information wird die erste (Teil-)Antwort dann schneller am Client ankommen, als dies bei der Versendung der gesamten Anfrage der Fall wäre."),
        Frage("Was ist eine Drei-Tier-Architektur für Client-ServerSysteme?", "dreischichtige Client-Server-Architektur besteht aus drei logischen Tiers, von denen jede im Prinzip auf einem anderen Computer implementiert ist:<br> - höchste Tier: Client-Benutzer-Interface<br> - mittleres Tier: enthält die eigentliche Anwendung <br>- unterste Tier: implementiert die benutzten Daten und deren Zugriff (z.B. eine Datenbank)"),
        Frage("Betrachten Sie eine Prozesskette P1, P2, ... , Pn, die eine Client-Server-Multitier-Architektur implementiert. Prozess Pi ist ein Client von Prozess Pi+1 und Pi gibt nur dann eine Antwort an Pi-1 zurück, wenn er eine Antwort von Pi+1 erhalten hat. Was sind die größten Probleme bei dieser Anordnung, wenn man die Anfrage-/Antwortleistung von Prozess Pi betrachtet?", "Performanz wird für große n sehr schlecht sein <br>Grund: Kommunikation zwischen zwei Schichten grundsätzlich zwischen zwei verschiedenen Rechnern <br> Performanz P1 hängt von den Anfrage-AntwortInteraktionen zwischen den anderen Schichten ab <br> weiteres Problem: Leistung durch schwächsten Glied in der Kette bestimmt (analog: Essensausgabe Mensa) <br> d.h. schlechte Performanz oder gar eine temporäre Nichterreichbarkeit eines Rechners in der Kette bestimmt die maximale Geschwindigkeit des gesamten Prozesses <br> Performanz auf der höchsten Schicht wird dadurch sofort beeinträchtigt"),
        Frage("Betrachten Sie ein BitTorrent-System, bei dem jeder Knoten über eine ausgehende Verbindung der Bandbreite Bout und eine eingehende Verbindung der Bandbreite Bin verfügt. Einige dieser Knoten (Seeds, also Samen) bieten freiwillig Dateien zum Herunterladen durch andere Knoten an. Was ist die maximale Download-Kapazität eines BitTorrent-Clients?", "zu beachten: ausgehende Kapazität der Seed-Knoten muss zwischen Clients aufgeteilt werden <br> Annahmen <br> - S Seeds und N Clients <br> - jeder Client wählt zufällig einen der Seed-Knoten  gesamte Ausgangskapazität der Seeds beträgt S × BOUT <br>  d.h. jedem Client stehen sofort S × BOUT / N DownloadKapazität von Seeds zur Verfügung<br>zusätzlich hilft jeder Client jedem anderen <br> d.h. jeder kann zusätzlich Teile von anderen Clients mit einer Geschwindigkeit von BOUT herunterladen <br>- Annahme: BIN > BOUT - aber: wegen der „Wie du mir, so ich dir“-Strategie wird Download-Kapazität eines Clients hauptsächlich durch seine ausgehende Kapazität bestimmt <br> gesamte Download-Kapazität ergibt sich zu: S × BOUT / N + BOUT"),
        Frage("Nennen Sie ein zwingendes (technisches) Argument, warum die „Wie Du mir, so ich Dir“-Strategie von BitTorrent weit davon entfernt ist, optimal für die gemeinsame Nutzung von Dateien im Internet zu sein.", "Normalerweise hohe Downloadrate und niedrige Uploadrate. BitTorrent berücksichtigt die Asymetrie nicht.")
        ]

kap3 = [
    Frage("Vergleichen Sie das Lesen einer Datei mithilfe eines Einzel- und eines Multithread-Dateiservers. Sofern sich die Daten in einem Cache des Arbeitsspeichers befinden, dauert es 15 ms, um eine Anforderung zu erhalten und zu verteilen sowie die restliche Verarbeitung durchzuführen. Wir nehmen an, dass in einem Drittel der Fälle eine Festplattenoperation notwendig ist. Dann kommen weitere 75 ms hinzu, in denen ein Thread ruht. <br> Wie viele Anforderungen pro Sekunde kann ein Singlethread-Server handhaben? <br> Wie viele sind es bei einem Multithread-Server?", "Einzelthread-Server <br> Annahme: 1 CPU  Antwortzeit pro Anfrage - Cache-Treffer: 15 ms - Cache-Fehlschläge: 75 + 15 = 90 ms <br> gewichteter Durchschnitt: 2/3 × 15 + 1/3 × 90  durchschnittliche Anfrage benötigt somit 40 ms <br> Server kann 25 Anfragen pro Sekunde bearbeiten <br> <br> Multithread-Server <br> Wartezeiten auf die Festplatte überlappen sich <br> d.h. jede Anfrage benötigt 15 ms <br> Server kann somit 1000/15 = 66,67 Anfragen pro Sekunde verarbeiten."),
    Frage("Ist es sinnvoll, die Anzahl der Threads in einem Serverprozess zu begrenzen?", "Ja, da begrenzte Speicherkapazität und Komplexität sonst zu hoch für BS ist, da Threads chaotisch operieren."),
    Frage("In der Vorlesung wurde ein Multithread-Server beschrieben und gezeigt, warum er besser ist als ein Singlethread-Server und ein Server nach dem Prinzip eines endlichen Zustandsautomaten. <br> Gibt es Umstände, unter denen ein Singlethread-Server besser ist? <br> Falls ja, nennen Sie ein Beispiel.", "Ja, wenn der Server nur den Prozessor beansprucht. Multithreading würde zu erhöhter Komplexität führen."),
    Frage("In X-Window wird das Terminal eines Benutzers als Server bezeichnet, während die Anwendung als Client bezeichnet wird. Ist das sinnvoll?", "Ja, der Server kontrolliert die Hardware und die Anwendungen können Anfragen stellen, die zu einer Manipulation führen, also sollte der X-Window Server auf dem Benutzercomputer mit der Grafikhardware liegen. Anwendungen sollten sich als Clients verhalten, die auf diese Grafikhardware zugreifen."),
    Frage("Das X-Protokoll leidet unter skalierbarkeitsproblemen. Wie können sie diese angehen?", "Verringerung der Bandbreite durch Benutzung von Kompressionstechniken. <br> Durch Cache Techniken kann Synchronisierungsverkehr reduziert werden.")
]

kap4 = [
    Frage("Ist ein Server, der eine TCP/IP-Verbindung unterhält, zustandslos oder zustandsbehaftet?", "Abhängig von der Betrachtungsweise. <br> wenn der Server keine anderen Informationen über den Client bereithält, könnte man argumentieren, dass der Server zustandslos sei <br> Grund, nicht der server selbst speichert den zustand des clients , sondern die transportschicht auf dem server. <br>"),
    Frage("Stellen Sie sich einen Webserver mit einer Tabelle vor, in der Client-IP-Adressen den Webseiten zugeordnet sind, auf die sie zuletzt zugegriffen haben. Wenn ein Client Verbindung mit diesem Server aufnimmt, schlägt dieser den Client in der Tabelle nach und gibt gegebenenfalls die registrierte Seite zurück. Ist dies ein zustandsloser oder zustandsbehafteter Server?", "<br> starke Argumente für einen zustandslosen Server <br> wichtiger Aspekt von zustandslosen Designs ist nicht, ob irgendwelche Informationen vom Server bereitgehalten werden, sondern ob diese Informationen für die Korrektheit erforderlich sind <br>- z.B. Synchronisation von Daten <br> vorliegendes Beispiel: selbst wenn Tabelle verloren geht, kann Interaktion eventuell immer noch stattfinden <br>- abhängig von der darüber ablaufenden Anwendung <br> in zustandsbehafteten Design wäre eine solche Interaktion nur möglich, nachdem sich der Server von diesem Defekt erholt hätte"),
    Frage("Stellen Sie sich einen Prozess P vor, der auf die Datei F zugreifen muss, wobei F sich lokal auf dem Computer befindet, auf dem P läuft. Wenn P auf einen anderen Rechner verschoben wird, muss er nach wie vor auf F zugreifen. Wie kann die systemweite Referenz auf F implementiert werden, wenn die Datei-Computer-Bindung fix ist?", "einfache Lösung: separaten Prozess Q zu erstellen, der entfernte Anfragen für F behandelt.<br> -Prozess P wird die gleiche Schnittstelle zu F bereitgestellt wie zuvor<br> -Prozess Q erscheint also im Prinzip wie ein Dateiserver, ist aber nur ein Vermittler eines Dateiservers"),
    Frage("Beschreiben Sie im Einzelnen, wie TCP-Pakete bei einem TCP-Handoff fließen. Gehen Sie dabei auch die Quellund Zieladressen in den verschiedenen Headern ein.", "TCP-Pakete von Clients werden basierend auf der IPAdresse des Paketes von einem Gerät angenommen (z.B. einem Transport-Layer-Switch)<br>Switch gibt Paket an geeigneten Server weiter (sog. TCP-Handoff)<br>- aber: weitergegebene Paket besitzt nicht notwendigerweise die IP-Adresse, die der Client angegeben hatte<br> antwortende Server setzt bei seinem Antwortpaket die Adresse des vom Client angesprochenen Servers ein, damit die Antwort wieder beim Client ankommt")
]

r = random
@app.route('/')
def hello():
    return "Hello"


@app.route('/1')
def kapitel_1():
    frage = r.randint(0, len(kap1) - 1)
    return kap1[frage].get_frage() + "<br>" + antwort(frage, kap1, 1) + menu() + addScript()

@app.route('/2')
def kapitel_2():
    frage = r.randint(0, len(kap2) - 1)
    return kap2[frage].get_frage() + "<br>" + antwort(frage, kap2, 2) + menu() + addScript()

@app.route('/3')
def kapitel_3():
    frage = r.randint(0, len(kap3) - 1)
    return kap3[frage].get_frage() + "<br>" + antwort(frage, kap3, 3) + menu() + addScript()

@app.route('/4')
def kapitel_4():
    frage = r.randint(0, len(kap4) - 1)
    return kap4[frage].get_frage() + "<br>" + antwort(frage, kap4, 4) + menu() + addScript()

if __name__ == '__main__':
    app.run()
