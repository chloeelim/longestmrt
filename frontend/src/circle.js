import { useEffect } from "react";

function Circle({
  id,
  cx,
  cy,
  r,
  fill,
  stroke,
  strokeWidth,
  strokeLinecap,
  path,
}) {
  id = id[2] === "0" ? id.substring(0, 2) + id.substring(3) : id;
  id = id.toUpperCase();
  useEffect(() => {
    const code_arr = path.filter((stations) =>
      stations.split(" ").includes(id)
    );
    const selected = code_arr.length > 0;
    const index = selected ? path.indexOf(code_arr[0]) : null;
    if (selected) {
      const func = () => {
        document.getElementById(id).style.fill = "orange";
      };
      const timeout = setTimeout(func, (index + 1.5) * 500);
      return () => clearTimeout(timeout);
    }
  }, [path]);

  return (
    <circle
      id={id}
      cx={cx}
      cy={cy}
      r={r}
      fill={fill}
      stroke={stroke}
      strokeWidth={strokeWidth}
      strokeLinecap={strokeLinecap}
    ></circle>
  );
}

export default Circle;
