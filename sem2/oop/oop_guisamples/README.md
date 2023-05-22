# Modul OOP - GUI Samples

Dieses Projekt enthält einige __Codebeispiele__ zur GUI-Programmierung im Modul OOP.
Es basiert auf dem __oop_maven_template__, welches für diesen Zweck leicht
modifiziert und vereinfacht wurde.

## Verwendung

Die  Projekt kann einfach kopiert und umbenannt werden. In NetBeans, IntelliJ und 
Visual Studio Code kann es **direkt** geoeffnet werden, in Eclipse  ist 
ein **Import** des Projektes (als `Existing Maven Project`) notwendig. 

### AWT-Beispiel

Da die AWT-API integrierter Bestandteil des JDKs ist, kann es direkt in der IDE
gestartet werden. Die Klasse

* ch.hslu.oop.exercise.gui.awt.__SwitchGuiAwtDemo__

enthält das vollständige Beispiel mit einer __main()__-Methode.

### Swing-Beispiele

Da die Swing-API integrierter Bestandteil des JDKs ist, kann es direkt in der IDE
gestartet werden. Die Klassen

* ch.hslu.oop.exercise.gui.swing.__SwitchGuiSwingDemo__
* ch.hslu.oop.exercise.gui.swing.__SwitchGuiSwingDemoLookAndFeel__

enthalten das identische Beispiel mit einer __main()__-Methode. Bei der 
Variante __LookAndFeel__-kann aber in der Main-Methode zusätzlich noch der 
Plattformstil verändert werden.

### OpenFX-/JavaFX-Beispiele
Die FX-Technologie wird als externe Library verwendet und verwendet zusätzlich
die mit Java 9 eingeführte Modularisierung. Ein einfacher Start direkt in der IDE
ist (ohne zusätzliche, spezifische Konfiguration) nicht so einfach möglich.
Darum bieten wir ihnen zwei Alternativen an:

* Start über Maven (in der Shell): `mvn javafx:run`
* Start als Shell-Script (Windows): `.\start.cmd`

In der zweiten Variante können Sie sich auch ansehen, wie der Start genau erfolgt.
Voraussetzung ist ein lokaler Build, so dass alle Dependencies (Thirdparties) 
lokal vorhanden sind.

## Bereits enhaltene Libraries (Dependencies)

* JUnit 5 - https://junit.org/junit5/
* JUnit Pioneer - https://junit-pioneer.org/
* AssertJ - https://assertj.github.io/doc/
* EqualsVerifier - https://jqno.nl/equalsverifier/
* Logging Framework - https://logging.apache.org/log4j/2.x/

## Integrierte Analysewerkzeuge (Code Qualitaet)

* Checkstyle - https://checkstyle.sourceforge.io/
* PMD - https://pmd.github.io/
* JaCoCo - https://www.eclemma.org/jacoco/
* Spotbugs - https://spotbugs.github.io/

## Weitere Integrationen (benoetigen ggf. Konfiguration/Account)

* [GitLab CI/CD](https://docs.gitlab.com/ee/ci/) (.gitlab-ci.yml) inkl. Coverageauswertung fuer Java.
* [AsciiDoctor-Plugin](https://asciidoctor.org/) fuer [AsciiDoc](https://asciidoc.org/)

Feedback und Fehlermeldungen willkommen: roland.gisler@hslu.ch
