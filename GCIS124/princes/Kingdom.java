import java.util.ArrayList;
import java.util.List;

public class Kingdom {
    private String name;
    private List<pwincess> pwincesses;
    private KingdomType type;

    public Kingdom(String name, KingdomType type) {
        this.name = name;
        this.type = type;
        this.pwincesses = new ArrayList<>();
    }

    public void addPrincess(pwincess pwincess) {
        pwincesses.add(pwincess);
    }

    public void printKingdomDetails() {
        System.out.println("Kingdom: " + name);
        System.out.println("Type: " + type + " (Climate: " + type.getClimate() + ")");
        for (pwincess pwincess : pwincesses) {
            System.out.println(pwincess);
        }
    }
}