

public class Connection {

    /**
     * Get Connection
     * @param connCtx
     * @return
     * @throws IOException
     */
    public static String connectionCall(ConnectionContext connCtx) throws IOException {
        
        Path path = Paths.get("D:/Work/생보부동산신탁/개발업무/DRM/1.002.xlsx");
        String name = "1.002.xlsx";
        String originalFilename = name;
        String contentType = "text/pain";
        byte[] content = Files.readAllBytes(path);
        MultipartFile newMFile = new MockMultipartFile(name, originalFilename, contentType, content);
    }
}