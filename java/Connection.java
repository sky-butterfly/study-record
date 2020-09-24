public class Connection {

    /**
     * Get Connection
     * @param connCtx
     * @return
     * @throws IOException
     */
    public static String connectionCall(ConnectionContext connCtx) throws IOException {
        
        BufferedReader in = null;
        URL obj = new URL(connCtx.getUrl());
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
           
        con.setRequestMethod(connCtx.getRequestMethod());
        
        ConnectionHeader[] headers = connCtx.getConnectionHeaders();
        for( ConnectionHeader h : headers ) {
            con.setRequestProperty(h.getKey(), h.getValue());
        }
        
        in = new BufferedReader(new InputStreamReader(con.getInputStream(), "UTF-8"));
        String result = in.lines().collect(Collectors.joining());
        
        return result;
    }
}