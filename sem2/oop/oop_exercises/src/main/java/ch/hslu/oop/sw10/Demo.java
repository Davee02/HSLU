package ch.hslu.oop.sw10;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Scanner;

public class Demo {
    private static final Logger LOG =
            LogManager.getLogger(Demo.class);

    public static void main(String[] args) {
        String input;
        Scanner scanner = new Scanner(System.in);

        do {
            System.out.print("Please input temperature (or 'exit' for terminating): ");
            input = scanner.next();

            try {
                float value = Float.parseFloat(input);
                Temperature temperature = Temperature.createFromCelsius(value);

                LOG.info("Temperature: {}°C", temperature.getTemperatureCelsius());
                LOG.info("Temperature: {} K", temperature.getTemperatureKelvin());
            } catch (NumberFormatException e) {
                if (!"exit".equals(input)) {
                    LOG.error("Invalid number input: {}", input, e);
                }
            } catch (IllegalArgumentException e) {
                LOG.error("Invalid temperature input: {}", input, e);
            }
        } while (!"exit".equals(input));

        LOG.info("Program terminated");
    }
}
