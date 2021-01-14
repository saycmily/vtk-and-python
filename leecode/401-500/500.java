import java.util.regex.*;

class RegexExample {
    public static void main(String[] args) {
        String line="11This order was placed for QT3000oOK?";
        String pattern="(\\D*)(\\d+)(\\w+)(\\d+)";
        //创建Pattern对象
        Pattern p=Pattern.compile(pattern);
        //创建Matcher对象
        Matcher m=p.matcher(line);
        if(m.find())
        {
            System.out.println("Found value: "+m.start());
            System.out.println("Found value: "+m.group(0));
            System.out.println("Found value: "+m.group(1));
            System.out.println("Found value: "+m.group(2));
            System.out.println("Found value: "+m.group(3));
        }
        else
        {
            System.out.println("No Match!");
        }
        int n=m.groupCount();
        System.out.println("一共有"+n+"个捕获组");
    }
}