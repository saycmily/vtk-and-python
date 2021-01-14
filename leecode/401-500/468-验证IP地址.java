class Solution {
    public String validIPAddress(String IP) {
        if (IP == null) {
            return "Neither";
        }
        
        String regex0 = "(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])";
        String regexIPv4 = regex0 + "(\\." + regex0 + "){3}";
        String regex1 = "([\\da-fA-F]{1,4})";
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
        Solution a = new Solution();
        String x = a.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334");
        System.out.println(x);
    }
}