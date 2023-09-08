import Rating from "@mui/material/Rating";
import "./Card.css";
import { useState } from "react";

export const Card = () => {
  const [options, setOptions] = useState([
    { option: "May include numbers", state: false },
    { option: "May include symbols", state: false },
    { option: "Must send the password hash", state: false },
    { option: "Must send a salted hash", state: false },
  ]);

  const [length, setLength] = useState<number>(1);
  const [password, setPassword] = useState<string>("");
  const [hash, setHash] = useState<string>("");
  const [rating, setRating] = useState<number>(0);

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

  const automaticClipboardSaving = (password: string) => {
    navigator.clipboard.writeText(password);
    const div = document.querySelector(".password-copied");
    div?.classList.add("visible");
    setTimeout(() => {
      div?.classList.remove("visible");
    }, 2000);
  };

  const calculateRatingValue = (rating: string) => {
    switch (rating) {
      case "Faible":
        return 1;
      case "Moyen":
        return 2.5;
      case "Fort":
        return 5;
    }
  };

  const handleGenerateClick = async () => {
    const len = length;
    const numbers = options[0].state ? 1 : 0;
    const symbols = options[1].state ? 1 : 0;
    const hash = options[2].state ? 1 : 0;
    const salt = options[3].state ? 1 : 0;

    const res = await fetch(
      `http://127.0.0.1:5000/password/${len}/${numbers}/${symbols}/${hash}/${salt}`
    );
    const resJson = await res.json();
    setPassword(resJson.response.password);
    setHash(resJson.response.hash);

    const mark = calculateRatingValue(resJson.response.rating);
    setRating(mark);

    handleOpacity();
    automaticClipboardSaving(resJson.response.password);
  };

  return (
    <>
      <div className="password-copied">Copied current password</div>
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
          <span className="password-title">Password length</span>
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
        <div className="password">
          {"Mot de passe: " + password} <br />
          {hash && "Hash: " + hash} <br />
          <Rating name="read-only" value={rating} readOnly className="rating" />
        </div>
        <button className="button" onClick={handleGenerateClick}>
          Generate
        </button>
      </div>
    </>
  );
};
