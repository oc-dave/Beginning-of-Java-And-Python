package Example1;

public class ocdave {
    public static String getInitials(String fullName) {
        StringBuilder initials = new StringBuilder();

        String[] names = fullName.split(" ");
        for (String name : names) {
            initials.append(name.charAt(0)).append(" ");
        }

        return initials.toString().trim();
    }
}

//package Example1;
//
//public class ocdave {
//    public static void main(String[] args) {
//        new ocdaveTest().testThatInitialsCanBeReturned();
//    }
//}
