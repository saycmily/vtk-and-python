class Solution468 {
    public String validIPAddress(String IP) {
        if (IP == null) {
            return "Neither";
        }
        
        String regex0 = "(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])";
        String regexIPv4 = regex0 + "(\\." + regex0 + "){3}";
        String regex1 = "[\\da-fA-F]{1,4}";
        String regexIPv6 = regex1 + "(:" + regex1 + "){7}";
        
        String result = "Neither";
        if (IP.matches(regexIPv4)) {
            result = "IPv4";
        } else if (IP.matches(regexIPv6)) {
            result = "IPv6";
        }
        return result;
    }

    public static void main(String[] args) {
        Solution468 a = new Solution468();
        String x = a.validIPAddress("172.16.254.1");
        System.out.println(x);
    }
}