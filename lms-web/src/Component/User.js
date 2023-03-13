export default function (prompt) {
  return (
    <div>
      <img
        src={prompt.photo}
        alt="Person"
        className="rounded cursor-pointer hover: w-32 h-32 "
      ></img>
    </div>
  );
}
