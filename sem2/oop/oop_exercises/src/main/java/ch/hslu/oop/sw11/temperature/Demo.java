package ch.hslu.oop.sw11.temperature;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Scanner;

public class Demo {
    private static final Logger LOG =
            LogManager.getLogger(Demo.class);

    public static void main(String[] args) {
        String input;
        Scanner scanner = new Scanner(System.in);
        TemperatureHistory history = new TemperatureHistory();
        history.addTemperatureExtremeListener(e -> onExtremeTemperatureReached(e));

        do {
            System.out.print("Please input temperature (or 'exit' for terminating): ");
            input = scanner.next();

            try {
                float value = Float.parseFloat(input);
                Temperature temperature = Temperature.createFromCelsius(value);
                history.add(temperature);

                LOG.info("Temperature: {}°C", temperature.getTemperatureCelsius());
                LOG.info("Temperature: {} K", temperature.getTemperatureKelvin());
            } catch (NumberFormatException e) {
                if (!"exit".equals(input)) {
                    LOG.error("Invalid input: {}", input, e);
                }
            } catch (IllegalArgumentException e) {
                LOG.error("Invalid temperature input: {}", input, e);
            }
        } while (!"exit".equals(input));

        LOG.info("Program terminated");
        LOG.info("# temperatures: {}", history.getCount());
        LOG.info("Average: {}°C", history.getAverage());
        LOG.info("Min: {}°C", history.getMin().getTemperatureCelsius());
        LOG.info("Max: {}°C", history.getMax().getTemperatureCelsius());
    }

    private static void onExtremeTemperatureReached(final TemperatureExtremeEvent event) {
        LOG.info("{} temperature reached: {}°C", event.getExtremeType(), event.getTemperature().getTemperatureCelsius());
    }
}
