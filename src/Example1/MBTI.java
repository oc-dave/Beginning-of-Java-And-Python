package Example1;

import java.util.Scanner;

public class MBTI {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] questions = new String[]{
                "1. At a party, do you:\nA. Interact with many, including strangers\nB. Interact with a few, known to you\n\n",
                "2. Are you more:\nA. Realistic than speculative\nB. Speculative than realistic\n\n",
                "3. Is it worse to:\nA. Have your head in the clouds\nB. Be too grounded in reality\n\n",
                "4. Are you more impressed by:\nA. Principles\nB. Emotions\n\n",
                "5. Are you more drawn toward the:\nA. Convincing\nB. Touching\n\n",
                "6. Do you prefer to work:\nA. To deadlines\nB. Just “whenever”\n\n",
                "7. Do you tend to choose:\nA. Rather carefully\nB. Somewhat impulsively\n\n",
                "8. At parties do you:\nA. Stay late, with increasing energy\nB. Leave early with decreased energy\n\n",
                "9. Are you more attracted to:\nA. Sensible people\nB. Imaginative people\n\n",
                "10. Are you more interested in:\nA. What is actual\nB. What is possible\n\n",
                "11. In judging others are you more swayed by:\nA. Laws than circumstances\nB. Circumstances than laws\n\n",
                "12. In approaching others is your inclination to be somewhat:\nA. Objective\nB. Personal\n\n",
                "13. Are you more:\nA. Punctual\nB. Leisurely\n\n",
                "14. Do you prefer:\nA. Many friends with brief contact\nB. A few friends with more lengthy contact\n\n",
                "15. Do you usually prefer:\nA. Doing things the usual way\nB. Doing things your own way\n\n",
                "16. Do you frequently daydream that you are:\nA. Some heroic person\nB. In some attractive place\n\n",
                "17. Are you more often:\nA.Mentally lost in thought\nB. A social butterfly\n\n",
                "18. Do you enjoy following:\nA. Familiar routines\nB. Unfamiliar routines\n\n",
                "19. Do you tend to:\nA. Speak easily and at length with strangers\nB. Find little to say to strangers\n\n",
                "20. Are you more likely to trust:\nA. Your experience\nB. Your hunch\n\n"
        };
        // declare an array to hold the user's responses
        char[] responses = new char[20];

        // iterate through the questions, prompting the user for a response and adding it to the responses array
        for (int i = 0; i < questions.length; i++) {
            char response;
            do {
                System.out.print(questions[i] + "Enter your answer (A/B): ");
                response = Character.toUpperCase(input.nextLine().charAt(0));
            } while (response != 'A' && response != 'B');
            responses[i] = response;
        }

        // display the user's responses
        System.out.println("\nYour responses:");
        for (int i = 0; i < responses.length; i++) {
            System.out.println((i+1) + ". " + responses[i]);
        }

        // determine the user's personality type based on their responses
        int e = 0, i = 0, s = 0, n = 0, t = 0, f = 0, j = 0, p = 0;
        for (int k = 0; k < responses.length; k += 2) {
            if (responses[k] == 'A') e++; else i++;
            if (responses[k+1] == 'A') s++; else n++;
        }
        for (int k = 0; k < responses.length; k += 4) {
            if (responses[k] == 'A') t++; else f++;
            if (responses[k+1] == 'A') j++; else p++;
        }
        String personality_type = "";
        if (e > i) personality_type += "E"; else personality_type += "I";
        if (s > n) personality_type += "S"; else personality_type += "N";
        if (t > f) personality_type += "T"; else personality_type += "F";
        if (j > p) personality_type += "J"; else personality_type += "P";
        // display the user's personality type
        System.out.println("Your personality type is " + personality_type);
        System.out.println("Thank you for taking the MBTI personality test!");

    }
}
