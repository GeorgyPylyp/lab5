
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class lab3zav1 {

    // Алфавіт згідно таблиці 1 (українські букви та цифри)
    private static final String ALPHABET = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ 0123456789";

    public static void main(String[] args) {

        BigInteger P = new BigInteger("59");
        BigInteger Q = new BigInteger("61");
        String message = "РАУТ03";

        // Крок 1: Обчислення n та φ(n)
        BigInteger n = P.multiply(Q);
        BigInteger phi = P.subtract(BigInteger.ONE).multiply(Q.subtract(BigInteger.ONE));

        // Крок 2: Вибір e (найбільше просте число, менше за P)
        BigInteger e = new BigInteger("53"); // Найбільше просте число < 59

        // Крок 3: Обчислення d
        BigInteger d = e.modInverse(phi);

        System.out.println("Відкритий ключ (e, n): (" + e + ", " + n + ")");
        System.out.println("Закритий ключ (d, n): (" + d + ", " + n + ")");

        // Крок 4: Шифрування повідомлення
        List<BigInteger> encrypted = encryptMessage(message, e, n);
        System.out.println("Шифрування повідомлення: \"" + message + "\"");
        for (int i = 0; i < message.length(); i++) {
            System.out.println(message.charAt(i) + " (" + (ALPHABET.indexOf(message.charAt(i)) + 1) +
                    ") -> " + encrypted.get(i));
        }

        // Крок 5: Дешифрування криптограми
        BigInteger[] crypto = {
                new BigInteger("1640"), new BigInteger("1705"),
                new BigInteger("2497"), new BigInteger("718"),
                new BigInteger("114"), new BigInteger("3256"),
                new BigInteger("1640"), new BigInteger("114")
        };

        System.out.print("\nДешифрування криптограми: ");
        for (BigInteger num : crypto) {
            System.out.print(num + " ");
        }
        System.out.println();

        String decrypted = decryptMessage(crypto, d, n);
        System.out.println("Розшифроване повідомлення: \"" + decrypted + "\"");

        // Додаткове завдання: ЕЦП
        System.out.println("\n=== ЕЛЕКТРОННИЙ ЦИФРОВИЙ ПІДПИС ===");
        computeAndVerifyDigitalSignature(message, e, d, n);
    }

    // Шифрування повідомлення
    private static List<BigInteger> encryptMessage(String message, BigInteger e, BigInteger n) {
        List<BigInteger> encrypted = new ArrayList<>();
        for (char c : message.toCharArray()) {
            int index = ALPHABET.indexOf(c) + 1;
            BigInteger m = new BigInteger(String.valueOf(index));
            BigInteger ciphered = m.modPow(e, n);
            encrypted.add(ciphered);
        }
        return encrypted;
    }

    // Дешифрування повідомлення
    private static String decryptMessage(BigInteger[] crypto, BigInteger d, BigInteger n) {
        StringBuilder decrypted = new StringBuilder();
        for (BigInteger ciphered : crypto) {
            BigInteger m = ciphered.modPow(d, n);
            int index = m.intValue() - 1;
            if (index >= 0 && index < ALPHABET.length()) {
                decrypted.append(ALPHABET.charAt(index));
            } else {
                decrypted.append("?");
            }
        }
        return decrypted.toString();
    }

    // Обчислення та перевірка ЕЦП
    private static void computeAndVerifyDigitalSignature(String message, BigInteger e, BigInteger d, BigInteger n) {
        // Обчислення хеш-образу
        BigInteger H = computeHash(message, n);
        System.out.println("Хеш-образ повідомлення: " + H);

        // Обчислення ЕЦП
        BigInteger S = H.modPow(d, n);
        System.out.println("ЕЦП (S): " + S);

        // Перевірка ЕЦП
        BigInteger H1 = S.modPow(e, n);
        System.out.println("Хеш з ЕЦП (H'): " + H1);

        BigInteger H2 = computeHash(message, n);
        System.out.println("Хеш отриманого повідомлення (H''): " + H2);

        if (H1.equals(H2)) {
            System.out.println("ЕЦП дійсний. Повідомлення не змінено.");
        } else {
            System.out.println("ЕЦП недійсний. Повідомлення змінено.");
        }

        // Перевірка зі зміненим повідомленням
        String alteredMessage = "РАУТ04"; // Змінюємо повідомлення
        BigInteger H3 = computeHash(alteredMessage, n);
        System.out.println("\nПеревірка зі зміненим повідомленням: \"" + alteredMessage + "\"");
        System.out.println("Хеш зміненого повідомлення: " + H3);

        if (H1.equals(H3)) {
            System.out.println("ПОМИЛКА: ЕЦП дійсний для зміненого повідомлення!");
        } else {
            System.out.println("ЕЦП недійсний для зміненого повідомлення - це правильно!");
        }
    }

    // Обчислення хеш-образу повідомлення
    private static BigInteger computeHash(String message, BigInteger n) {
        BigInteger H = BigInteger.ZERO;
        for (char c : message.toCharArray()) {
            int M = ALPHABET.indexOf(c) + 1;
            BigInteger temp = H.add(new BigInteger(String.valueOf(M)));
            H = temp.multiply(temp).mod(n);
        }
        return H;
    }
}