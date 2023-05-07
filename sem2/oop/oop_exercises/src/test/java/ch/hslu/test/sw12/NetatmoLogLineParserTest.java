package ch.hslu.test.sw12;

import ch.hslu.oop.sw12.Measurement;
import ch.hslu.oop.sw12.NetatmoLogLineParser;
import org.junit.jupiter.api.Test;

import java.time.format.DateTimeParseException;

import static org.assertj.core.api.Assertions.*;

public class NetatmoLogLineParserTest {
    @Test
    void testParseLine() {
        // arrange
        NetatmoLogLineParser parser = new NetatmoLogLineParser();

        // act
        Measurement measurement = parser.parseLine("1517009945;\"2023/01/27 00:39:05\";6.4;78");

        // assert
        assertThat(measurement.getTemperature().getTemperatureCelsius()).isEqualTo(6.4d, offset(0.0001d));
        assertThat(measurement.getTimestamp()).isEqualTo("2023-01-27T00:39:05");
    }

    @Test
    void testParseLineWithInvalidTimestamp() {
        // arrange
        NetatmoLogLineParser parser = new NetatmoLogLineParser();

        // assert
        assertThatThrownBy(() -> parser.parseLine("1517009945;\"2023/01 00:39:05\";6.4;78"))
                .isInstanceOf(DateTimeParseException.class);
    }

    @Test
    void testParseLineWithInvalidTemperature() {
        // arrange
        NetatmoLogLineParser parser = new NetatmoLogLineParser();

        // assert
        assertThatThrownBy(() -> parser.parseLine("1517009945;\"2023/01/27 00:39:05\";6.4a;78"))
                .isInstanceOf(NumberFormatException.class);
    }
}
