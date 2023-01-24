// import axios from "axios";
import { push } from "connected-react-router";
import { toast } from "react-toastify";
import { SET_TOKEN, SET_CURRENT_USER, UNSET_CURRENT_USER } from "./LoginTypes";
import { toastOnError } from "../../utils/Utils";
import { setAxiosAuthToken } from "../../utils/Axios";
import axiosInstance from "../../utils/Axios";

export const login = (userData, redirectTo) => dispatch => {
  axiosInstance
    // .post("/api/token", JSON.stringify(userData))
    .post("/api/token", userData)
    .then(response => {
      // console.log(response.data);
      // console.log(response.data.access);
      // console.log(typeof response.data.access)

      const auth_token = response.data.access;

      setAxiosAuthToken(response.data);
      dispatch(setToken(auth_token));
      dispatch(getCurrentUser(auth_token, redirectTo));
    })
    .catch(error => {
      dispatch(unsetCurrentUser());
      toastOnError(error);
    });
};



export const getCurrentUser = (auth_token, redirectTo) => dispatch => {
  axiosInstance
    .get("/api/v1/users/auth/user",
    )
    .then(response => {
      const user = {
        username: response.data.username,
        email: response.data.email
      };
      dispatch(setCurrentUser(user, redirectTo));
    })
    .catch(error => {
      dispatch(unsetCurrentUser());
      if (error.response) {
        if (
          error.response.status === 401 &&
          error.response.hasOwnProperty("data") &&
          error.response.data.hasOwnProperty("detail") &&
          error.response.data["detail"] === "User inactive or deleted."
        ) {
          dispatch(push("/resend_activation"));
        }
      } else {
        toastOnError(error);
      }
    });
};

export const setCurrentUser = (user, redirectTo) => dispatch => {
  localStorage.setItem("user", JSON.stringify(user));
  dispatch({
    type: SET_CURRENT_USER,
    payload: user
  });

  if (redirectTo !== "") {
    dispatch(push(redirectTo));
  }
};

export const setToken = token => dispatch => {
  // setAxiosAuthToken(token);
  localStorage.setItem("access_token", token);
  dispatch({
    type: SET_TOKEN,
    payload: token
  });
};

export const unsetCurrentUser = () => dispatch => {
  // setAxiosAuthToken("");
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  axiosInstance.defaults.headers['Authorization'] = null;
  dispatch({
    type: UNSET_CURRENT_USER
  });
};

export const logout = () => dispatch => {
  axiosInstance
    .post("/api/v1/users/auth/logout")
    .then(response => {
      dispatch(unsetCurrentUser());
      dispatch(push("/"));
      toast.success("Logout successful.");
    })
    .catch(error => {
      dispatch(unsetCurrentUser());
      toastOnError(error);
    });
};