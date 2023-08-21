enum NORTH_CENTRAL {
    BENUE,
    KOGI,
    KWARA,
    NASARAWA,
    NIGER,
    PLATEAU,
    FEDERAL_CAPITAL_TERRITORY
}

enum NORTH_EAST {
    ADAMAWA,
    BAUCHI,
    BORNO,
    GOMBE,
    TARABA,
    YOBE
}

enum NORTH_WEST {
    JIGAWA,
    KADUNA,
    KANO,
    KATSINA,
    KEBBI,
    SOKOTO,
    ZAMFARA
}

enum SOUTH_EAST {
    ABIA,
    ANAMBRA,
    EBONYI,
    ENUGU,
    IMO
}
enum SOUTH_SOUTH {
    AKWA_IBOM,
    BAYELSA,
    CROSS_RIVER,
    DELTA,
    EDO,
    RIVERS_STATE
}

 enum SOUTH_WEST {
    EKITI,
    LAGOS,
    OGUN,
    ONDO,
    OSUN,
    OYO_STATES
}
public class
Geopolitical_Zones {
    public static void main(String[] args) {
        for (SOUTH_SOUTH southSouth : SOUTH_SOUTH.values()) {
            System.out.println(southSouth);
            System.out.printf("\n");
        }

//        for (NORTH_WEST northWest : NORTH_WEST.values()) {
//            System.out.println(northWest);
        }
    }


