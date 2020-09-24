public class FileUtils {

    /**
     * 바이트 => 바이너리 텍스트
     * @param n
     * @return
     */
    public static String ToBinaryText(byte b) {
        StringBuilder sb = new StringBuilder("00000000");
        for (int bit = 0; bit < 8; bit++) {
            if (((b >> bit) & 1) > 0) {
                sb.setCharAt(7 - bit, '1');
            }
        }
        return sb.toString();
    }
    
    /**
     * 바이트 배열 => 바이너리 텍스트
     * @param b
     * @return
     */
    public static String ToBinaryText(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < bytes.length; ++i) {
            sb.append(ToBinaryText(bytes[i]));
        }
        return sb.toString();
    }
        
    /**
     * 파일 패스 => 바이너리 텍스트
     * @param file
     * @return
     * @throws Exception
     */
    public static String toBinaryText(String filePath) throws Exception {
        
        byte[] bytes = ToByteArray(filePath);
        String binaryText = ToBinaryText(bytes);
        
        return binaryText;
    }
    
    /**
     * 파일 패스 => 바이트 배열
     * @param filePath
     * @return
     * @throws IOException 
     */
    public static byte[] ToByteArray(String filePath) throws IOException {
        
        FileInputStream fileInputStream = null;
        byte[] bytes = null;
        
        File file = new File(filePath);
        bytes = new byte[(int) file.length()];
        
        fileInputStream = new FileInputStream(file);
        fileInputStream.read(bytes);
        
        return bytes;
    }
    
    /**
     * 바이너리 텍스트 => 바이트
     * @param binaryText
     * @return
     */
    private static byte fromBinaryTextToByte(String binaryText) {
        byte ret = 0, total = 0;
        for(int i=0; i<8; ++i) {
            ret = (binaryText.charAt(7-i)=='1') ? (byte)(1 << i) : 0;
            total = (byte) (ret | total);
        }
        return total;
    }
    
    /**
     * 바이너리 텍스트 => 바이트 배열
     * @param binaryText
     * @return
     */
    public static byte[] fromBinaryText(String binaryText) {
        int cnt = binaryText.length() / 8;
        byte[] bytes = new byte[cnt];
        
        for(int i=1; i<cnt; ++i) {
            String text = binaryText.substring((i-1) * 8, i * 8);
            bytes[i-1] = fromBinaryTextToByte(text);
        }
        return bytes;
    }
}