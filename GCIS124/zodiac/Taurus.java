public class Taurus extends Zodiac {

    public Taurus() {
        super("Taurus", "Apr 20 - May 20");
    }

    @Override
    public String toString() {
        return super.toString() + " Taurus are known for being patient!";
    }


    
    public static void main(String[] args) {
        Taurus t = new Taurus();
        System.out.println(t);
    }
}
