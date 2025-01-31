import java.io.BufferedReader;
import java.io.FileReader;

/* https://adventofcode.com/2020/day/2

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
*/

class PasswordWithPolicy {
    int minCharCount;
    int maxCharCount;
    String password;
    Character c;
}

public class DayTwo {
    public static void main(String[] args) throws Exception {
        int numberOfValidPasswords = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("day_2_input.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
               if (isPasswordValidPart2(line)) {
                numberOfValidPasswords++;
               }
            }
        }

        // String[] input = new String[] {"1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"};
        // int numberOfValidPasswords = countValidPasswords(input);
        System.out.println(numberOfValidPasswords);
    }

    private static int countValidPasswords(String[] passwordsWithPolicies) {
        int count = 0;
        for(String passwordWithPolicy: passwordsWithPolicies) {
            if (isPasswordValidPart2(passwordWithPolicy)) {
                count++;
            }
        }
        return count;
    }



    private static PasswordWithPolicy parsePasswordPolicy(String passwordWithPolicy) {
        String[] parts = passwordWithPolicy.split(": ");
        String policy =parts[0]; //"N-X C"
        String password = parts[1];

        String[] policyRangeAndChar = policy.split(" ");
        String range = policyRangeAndChar[0];
        String c = policyRangeAndChar[1];

        String[] minMax = range.split("-");
        int min = Integer.parseInt(minMax[0]);
        int max = Integer.parseInt(minMax[1]);

        PasswordWithPolicy parsed = new PasswordWithPolicy();
        parsed.c = c.charAt(0);
        parsed.password = password;
        parsed.minCharCount = min;
        parsed.maxCharCount = max;

        return parsed;
    }

    private static boolean isPasswordValid(String passwordWithPolicy) {
        PasswordWithPolicy parsed = parsePasswordPolicy((passwordWithPolicy));
        int counter = 0;
        for(char c: parsed.password.toCharArray()) {
            if (c == parsed.c) {
                counter++;
            }

            if (counter > parsed.maxCharCount) {
                return false;
            }
        }

        if (counter < parsed.minCharCount) {
            return false;
        }

        return true;
    }

    private static boolean isPasswordValidPart2(String passwordWithPolicy) {
        PasswordWithPolicy parsed = parsePasswordPolicy((passwordWithPolicy));
        //kinda XOR 
        boolean firstPositionMatchesChar = parsed.password.charAt(parsed.minCharCount -1) == parsed.c;
        boolean secondPositionMatchesChar = parsed.password.charAt(parsed.maxCharCount -1) == parsed.c;

        return firstPositionMatchesChar ^ secondPositionMatchesChar;
    }


}