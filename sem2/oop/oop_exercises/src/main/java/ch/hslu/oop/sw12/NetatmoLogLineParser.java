package ch.hslu.oop.sw12;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class NetatmoLogLineParser implements ILogLineParser {
    @Override
    public Measurement parseLine(String line) throws DateTimeParseException, NumberFormatException {
        String[] splittedLine = line.split(";");

        double temperatureValue = Double.parseDouble(splittedLine[2]);
        Temperature temperature = Temperature.createFromCelsius(temperatureValue);

        LocalDateTime timestamp =
                LocalDateTime.parse(splittedLine[1],
                        DateTimeFormatter.ofPattern("\"yyyy/MM/dd HH:mm:ss\""));

        return new Measurement(temperature, timestamp);
    }
}
