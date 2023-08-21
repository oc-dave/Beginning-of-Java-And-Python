package Example1;

public enum GPS {
    NORTH_CENTRAL("BENUE, KOGI, KWARA, NASARAWA, NIGER, PLATEAU, FCT"),
    NORTH_EAST("ADAMAWA, BAUCHI, BORNO, GOMBE, TARABA, YOBE"),
    NORTH_WEST("JIGAWA, KADUNA, KANO, KATSINA, KEBBI, SOKOTO, ZAMFARA"),
    SOUTH_EAST("ABIA, ANAMBRA, EBONYI, ENUGU, IMO"),
    SOUTH_SOUTH("AKWA_IBOM, BAYELSA, CROSS_RIVER, DELTA, EDO, RIVERS"),
    SOUTH_WEST("EKITI, LAGOS, OGUN, ONDO, OSUN, OYO");

    private String states;

    GPS(String states) {
        this.states = states;
    }

    public String getStates() {
        return states;
    }

    public void setStates(String states) {
        this.states = states;
    }

    public static GPS getGPSState(String state) {
        for (GPS gps : GPS.values()) {
            String[] states = gps.getStates().split(", ");
            for (String s : states) {
                if (s.equalsIgnoreCase(state)) {
                    return gps;
                }
            }
        }
        return null;
    }
}
