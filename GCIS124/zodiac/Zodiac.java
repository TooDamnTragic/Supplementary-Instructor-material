public class Zodiac {
    private String name;
    private String dateRange;

    public Zodiac(String name, String dateRange) {
        this.name = name;
        this.dateRange = dateRange;
    }

    public String getName() {
        return name;
    }

    public String getDateRange() {
        return dateRange;
    }


    @Override
    public String toString() {
        return "Zodiac Sign: " + name + ", Date Range: " + dateRange;
    }



    public static void main(String[] args) {
        Zodiac z = new Zodiac("JinxSign", "July 1 - July 2");
        System.out.println(z);
    }
}
