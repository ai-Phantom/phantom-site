export async function onRequest(context) {
  const { request, next } = context;
  const url = new URL(request.url);
  
  if (url.pathname.startsWith('/api/')) {
    const backendUrl = 'https://phantom-traders-backend.onrender.com' + 
                       url.pathname.replace('/api', '') + 
                       url.search;
    
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': '*',
        }
      });
    }
    
    const newRequest = new Request(backendUrl, {
      method: request.method,
      headers: request.headers,
      body: request.method !== 'GET' ? request.body : undefined,
    });
    
    const response = await fetch(newRequest);
    const newResponse = new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: response.headers,
    });
    newResponse.headers.set('Access-Control-Allow-Origin', '*');
    return newResponse;
  }
  
  return next();
}
