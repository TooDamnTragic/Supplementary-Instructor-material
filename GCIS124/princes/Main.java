
public class Main {
    public static void main(String[] args) {
        Kingdom kingdom = new Kingdom("Arendelle", KingdomType.WATER);
        pwincess anna = new pwincess("Anna", "Arendelle", 18);
        pwincess elsa = new pwincess("Elsa", "Arendelle", 21);

        kingdom.addPrincess(anna);
        kingdom.addPrincess(elsa);

        kingdom.printKingdomDetails();
    }
}