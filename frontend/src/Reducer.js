import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";

import { loginReducer } from "./components/login/LoginReducer";
import { notesReducer } from "./components/movies/MoviesReducer";

const createRootReducer = history =>
  combineReducers({
    router: connectRouter(history),
    auth: loginReducer,
    notes: notesReducer
  });

export default createRootReducer;
