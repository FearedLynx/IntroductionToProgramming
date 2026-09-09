public class Lecture2 {
    public static void main(String[] args) {
        int adult_ticket = 120;
        int student_ticket = 80;
        int adult_count = 85;
        int student_count = 64;

        int adult_revenue = adult_ticket * adult_count;
        int student_revenue = student_ticket * student_count;
        int total_tickets = adult_count + student_count;
        int total_revenue = adult_revenue + student_revenue;
        double average_revenue = total_revenue / (double) total_tickets;

        System.out.println("Adult revenue: " + adult_revenue);
        System.out.println("Student revenue: " + student_revenue);
        System.out.println("Total tickets: " + total_tickets);
        System.out.println("Total revenue: " + total_revenue);
        System.out.println("Average revenue per ticket: " + average_revenue);
    }
}
