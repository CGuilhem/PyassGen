import "./Card.css";
import { useState } from "react";

export const Card = () => {
  const [options, setOptions] = useState([
    { option: "Must include numbers", state: false },
    { option: "Must include symbols", state: false },
    { option: "Must send the password hash", state: false },
  ]);

  const [length, setLength] = useState<number>(1);
  const [password, setPassword] = useState<string>("");

  const handleChange = (state: boolean, i: number) => {
    const tmp = options[i];
    tmp.state = !state;
    const optionsClone = [...options];
    optionsClone[i] = tmp;
    setOptions([...optionsClone]);
  };

  const handleOpacity = () => {
    const divpass = document.querySelector(".password");
    divpass?.classList.add("visible");
  };

  const handleGenerateClick = async () => {
    const len = length;
    const numbers = options[0].state ? 1 : 0;
    const symbols = options[1].state ? 1 : 0;
    // const hash = options[2].state ? 1 : 0;

    const res = await fetch(
      `http://127.0.0.1:5000/password/${len}/${numbers}/${symbols}`
    );
    const resJson = await res.json();
    setPassword(resJson.response.password);

    handleOpacity();
  };

  return (
    <>
      <div className="card">
        <h1 className="title">PYassGen</h1>
        {options.map(({ option, state }, i) => (
          <div key={i}>
            <label htmlFor={i.toString()}>
              <input
                type="checkbox"
                onChange={() => handleChange(state, i)}
                checked={state}
                id={i.toString()}
              />
              <span className="option">{option}</span>
            </label>
          </div>
        ))}
        <div className="input-length">
          <span>Password length</span>
          <input
            type="number"
            className="input-number"
            pattern="[0-9]*"
            value={length}
            onChange={(e) =>
              setLength((v) =>
                e.target.validity.valid ? parseInt(e.target.value) : v
              )
            }
          />
        </div>
        <div className="password">{password}</div>
        <button className="button" onClick={handleGenerateClick}>
          Generate
        </button>
      </div>
    </>
  );
};
