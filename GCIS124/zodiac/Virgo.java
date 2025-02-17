public class Virgo extends Zodiac {

    public Virgo() {
        super("Virgo", "Aug 23 - Sep 22");
    }

    @Override
    public String toString() {
        return super.toString() + " Virgos are not known!";
    }
    public static void main(String[] args) {
        Virgo V = new Virgo();
System.out.println(V);
    }
}
