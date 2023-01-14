import "./App.css";
import {
  Box,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Button,
} from "@mui/material";
import { useState } from "react";
import axios from "axios";
import Map from "./map";

function App() {
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [data, setData] = useState({});
  const [path, setPath] = useState([]);

  useState(() => {
    axios
      .get("http://127.0.0.1:5001/mrts", {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      })
      .then((res) => setData(res.data));
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    document.querySelectorAll("circle").forEach((circle) => {
      circle.style.fill = "white";
    });
    axios
      .get("http://127.0.0.1:5001/longest", {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
        params: {
          s: start,
          e: end,
        },
      })
      .then((res) => {
        setPath(res.data.path);
      });
  }

  return (
    <div id="app">
      <aside
        style={{
          backgroundColor: "lightblue",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
        }}
      >
        <form onSubmit={handleSubmit}>
          <Box sx={{ m: 1, display: "flex", flexDirection: "column", gap: 1 }}>
            <FormControl fullWidth>
              <InputLabel>Start</InputLabel>
              <Select
                value={start}
                label="Start"
                onChange={(e) => setStart(e.target.value)}
              >
                {Object.entries(data).map(([k, v]) => (
                  <MenuItem value={k}>{v + ` (${k})`}</MenuItem>
                ))}
              </Select>
            </FormControl>
            <FormControl fullWidth>
              <InputLabel>End</InputLabel>
              <Select
                value={end}
                label="Start"
                onChange={(e) => setEnd(e.target.value)}
              >
                {Object.entries(data).map(([k, v]) => (
                  <MenuItem value={k}>{v + ` (${k})`}</MenuItem>
                ))}
              </Select>
            </FormControl>
            <Button variant="contained" color="primary" type="submit">
              Submit
            </Button>
            {JSON.stringify(path)}
          </Box>
        </form>
      </aside>
      <main>
        {console.log(path)}
        <Map path={path} />
      </main>
    </div>
  );
}

export default App;
