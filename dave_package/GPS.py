class GPS:
    NORTH_CENTRAL = "benue, kogi, kwara, nasarawa, niger, plateau, fct"
    NORTH_EAST = "adamawa, bauchi, borno, gombe, taraba, yobe"
    NORTH_WEST = "jigawa, kaduna, kano, katsina, kebbi, sokoto, zamfara"
    SOUTH_EAST = "abia, anambra, ebonyi, enugu, imo"
    SOUTH_SOUTH = "akwa_ibom, bayelsa, cross_river, delta, edo, rivers"
    SOUTH_WEST = "ekiti, lagos, ogun, ondo, osun, oyo"


class Gps:
    @staticmethod
    def get_GPS_state(state):
        lowercase_state = state.lower()
        if lowercase_state in GPS.NORTH_CENTRAL:
            return "NORTH_CENTRAL"
        elif lowercase_state in GPS.NORTH_EAST:
            return "NORTH_EAST"
        elif lowercase_state in GPS.NORTH_WEST:
            return "NORTH_WEST"
        elif lowercase_state in GPS.SOUTH_EAST:
            return "SOUTH_EAST"
        elif lowercase_state in GPS.SOUTH_SOUTH:
            return "SOUTH_SOUTH"
        elif lowercase_state in GPS.SOUTH_WEST:
            return "SOUTH_WEST"
        else:
            return None

    @staticmethod
    def Result():
        state = input("Enter your state: ")
        gps = Gps.get_GPS_state(state)

        if gps:
            print(f"Geopolitical zone: {gps}")
        else:
            print("Invalid State entered!")


Gps.Result()

