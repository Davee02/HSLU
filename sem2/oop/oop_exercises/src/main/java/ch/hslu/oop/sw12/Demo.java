package ch.hslu.oop.sw12;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.time.format.DateTimeParseException;

public class Demo {
    private static final Logger LOG =
            LogManager.getLogger(ch.hslu.oop.sw11.temperature.Demo.class);

    public static void main(String[] args) {
        String filePath = ".\\src\\main\\resources\\netatmo-export-202301-202304.csv";
        if (!Files.exists(Paths.get(filePath))) {
            LOG.error("File not found");
            return;
        }

        MeasurementHistory history = new MeasurementHistory();
        ILogLineParser parser = new NetatmoLogLineParser();
        try (BufferedReader br =
                     new BufferedReader(new InputStreamReader(
                             new FileInputStream(filePath), StandardCharsets.UTF_8))
        ) {
            String line;
            while ((line = br.readLine()) != null) {
                try {
                    Measurement measurement = parser.parseLine(line);
                    history.add(measurement);
                } catch (DateTimeParseException | NumberFormatException e) {
                    LOG.error(e.getMessage(), e);
                }
            }
        } catch (IOException ioe) {
            LOG.error(ioe.getMessage(), ioe);
        }

        LOG.info("Min temperature was {}°C which was reached at {}", history.getMin().getTemperature().getTemperatureCelsius(), history.getMin().getTimestamp());
        LOG.info("Max temperature was {}°C which was reached at {}", history.getMax().getTemperature().getTemperatureCelsius(), history.getMax().getTimestamp());
        LOG.info("Average temperature was {}°C", history.getAverage());
    }
}
