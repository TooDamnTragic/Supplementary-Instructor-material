public class Aries extends Zodiac {

    public Aries() {
        super("Aries", "Mar 21 - Apr 19");
    }

    @Override
    public String toString() {
        return super.toString() + " Aries are known for being bold!";
    }

    public static void main(String[] args) {
        Aries a = new Aries();
        System.out.println(a);
    }
}
