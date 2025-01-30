public enum KingdomType {
    AIR("Cold"), WATER("Humid"),
    EARTH("Temperate"), FIRE("Arid"),
    MUSHROOM("High");
    
    private final String climate;

    KingdomType(String climatee) {
        this.climate = climatee;
    }

    public String getClimate() {
        return climate;
    }
}
