import "./App.css";
import logo from "./stupidsmrtlogo.svg";
import {
  Box,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Button,
  Typography,
  Slider,
  ToggleButtonGroup,
  ToggleButton,
} from "@mui/material";
import { useState } from "react";
import axios from "axios";
import Map from "./map";
import ShortcutIcon from "@mui/icons-material/Shortcut";
import RoundAboutRightIcon from "@mui/icons-material/RoundaboutRight";

function App() {
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [data, setData] = useState({});
  const [path, setPath] = useState([]);
  const [shortest, setShortest] = useState(true);
  const [delay, setDelay] = useState(500);
  const [loading, setLoading] = useState(false);

  useState(() => {
    axios
      .get(`${process.env.REACT_APP_BACKEND_URL}/mrts`, {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      })
      .then((res) => setData(res.data));
  }, []);

  function replay() {
    document.querySelectorAll("circle").forEach((circle) => {
      circle.style.fill = "white";
    });
    setTimeout(() => setPath([...path]), 500);
  }

  function handleSubmit(e) {
    e.preventDefault();
    document.querySelectorAll("circle").forEach((circle) => {
      circle.style.fill = "white";
    });
    setLoading(true);
    axios
      .get(
        shortest
          ? `${process.env.REACT_APP_BACKEND_URL}/shortest`
          : `${process.env.REACT_APP_BACKEND_URL}/longest`,
        {
          headers: {
            "Access-Control-Allow-Origin": "*",
          },
          params: {
            s: start,
            e: end,
          },
        }
      )
      .then((res) => {
        setPath(res.data.path);
        setLoading(false);
      });
  }

  function handleSetShortest(e, newValue) {
    if (newValue !== null) {
      setShortest(newValue);
    }
  }

  return (
    <div id="app">
      <aside
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
        }}
      >
        <img
          src={logo}
          alt="stupid mrt logo"
          style={{ width: "300px", alignSelf: "center" }}
        />
        <form onSubmit={handleSubmit}>
          <Box sx={{ m: 1, display: "flex", flexDirection: "column", gap: 1 }}>
            <FormControl fullWidth>
              <InputLabel>Start</InputLabel>
              <Select
                value={start}
                label="Start"
                onChange={(e) => setStart(e.target.value)}
                sx={{ backgroundColor: "#ffffe5" }}
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
                sx={{ backgroundColor: "#ffffe5" }}
              >
                {Object.entries(data).map(([k, v]) => (
                  <MenuItem value={k}>{v + ` (${k})`}</MenuItem>
                ))}
              </Select>
            </FormControl>
            <Box sx={{ display: "flex", gap: 1, alignItems: "center" }}>
              <ToggleButtonGroup
              value={shortest}
              exclusive
              onChange={handleSetShortest}>
                <ToggleButton value={true} aria-label="shortest path">
                  <ShortcutIcon /> Shortest Path
                </ToggleButton>

                <ToggleButton value={false} aria-label="shortest path">
                  <RoundAboutRightIcon /> Longest Path
                </ToggleButton>
              </ToggleButtonGroup>
            </Box>
            <Box sx={{ display: "flex", gap: 1, alignItems: "center" }}>
              <Slider
                defaultValue={500}
                value={delay}
                onChange={(e) => setDelay(e.target.value)}
                step={50}
                marks
                min={250}
                max={1000}
              />
              <Typography>Delay</Typography>
            </Box>

            <Button variant="contained" color="primary" type="submit">
              Submit
            </Button>
            <Button variant="contained" color="secondary" onClick={replay}>
              Replay
            </Button>
            {path.length > 0 && (
              <Box
                sx={{
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  justifyContent: "center",
                }}
              >
                <Typography variant="h2">{path.length}</Typography>
                <Typography variant="h5">stations</Typography>
              </Box>
            )}
          </Box>
        </form>
      </aside>
      <main>
        {console.log(path)}
        <Map path={path} delay={delay} loading={loading} />
      </main>
    </div>
  );
}

export default App;
