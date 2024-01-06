import axios from "axios";

const client = axios.create({
  baseURL: process.env.REACT_APP_BACKEND_URL,
  headers: {
    "Access-Control-Allow-Origin": "*",
  },
});

class API {
  async getAllMrts() {
    const response = await client.get("/mrts", {});
    return response.data;
  }

  async getShortestPath(start, end) {
    const response = await client.get("/shortest", {
      params: {
        s: start,
        e: end,
      },
    });
    return response.data.path;
  }

  async getLongestPath(start, end) {
    const response = await client.get("/longest", {
      params: {
        s: start,
        e: end,
      },
    });
    return response.data.path;
  }
}

const api = new API();
export default api;
