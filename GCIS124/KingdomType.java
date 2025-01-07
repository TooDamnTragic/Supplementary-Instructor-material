public enum KingdomType {
    AIR("Cold"), WATER("Humid"), EARTH("Temperate"), FIRE("Arid"), MUSHROOM("High");
    
    private final String climate;

    KingdomType(String climate) {
        this.climate = climate;
    }

    public String getClimate() {
        return climate;
    }
}
