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
  console.log(path);
  console.log(path.map((stations) => stations.split(" ")));
  id = id[2] == "0" ? id.substring(0, 2) + id.substring(2) : id;
  id = id.toUpperCase();
  console.log({ id });
  const selected =
    path.filter((stations) => stations.split(" ").includes(id)).length > 0;
  console.log({ selected });
  return (
    <circle
      id={id}
      cx={cx}
      cy={cy}
      r={r}
      fill={selected ? "orange" : fill}
      stroke={stroke}
      strokeWidth={strokeWidth}
      strokeLinecap={strokeLinecap}
    ></circle>
  );
}

export default Circle;
