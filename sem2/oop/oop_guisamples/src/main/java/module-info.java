/*
 * Copyright 2022 Hochschule Luzern - Informatik.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Modul für OOP-GUI-Samples.
 */
module ch.hslu.oop.exercise.guisamples {

    requires java.desktop;

    requires javafx.controls;
    requires javafx.graphics;
    requires javafx.base;
    requires javafx.fxml;

    requires org.apache.logging.log4j;

    opens ch.hslu.oop.exercise.common;
    opens ch.hslu.oop.exercise.gui.javafx;
    opens ch.hslu.oop.exercise.gui.javafxml;

    exports ch.hslu.oop.exercise.gui.javafxml to javafx.fxml;
}
