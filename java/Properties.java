public class Properties {

    /**
     * 프로퍼티 파일 접근
     * @param resource
     * @return
     * @throws IOException
     */
    public static Properties getProperties(String resource) throws IOException {
        
        Properties props = new Properties();
        InputStream is = new FileInputStream(resource);
        props.load(is);
        
        return props;
    }
}