// import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_MOVIES, ADD_MOVIE, DELETE_MOVIE, UPDATE_MOVIE } from "./MoviesTypes";
import axiosInstance from "../../utils/Axios";

export const getNotes = () => dispatch => {
  axiosInstance
    .get("/api/v1/movie")
    .then(response => {
      dispatch({
        type: GET_MOVIES,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const addNote = note => dispatch => {
  axiosInstance
    .post("/api/v1/movie", note)
    .then(response => {
      dispatch({
        type: ADD_MOVIE,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const deleteNote = id => dispatch => {
  axiosInstance
    .delete(`/api/v1/movie${id}`)
    .then(response => {
      dispatch({
        type: DELETE_MOVIE,
        payload: id
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const updateNote = (id, note) => dispatch => {
  axiosInstance
    .patch(`/api/v1/movie${id}`, note)
    .then(response => {
      dispatch({
        type: UPDATE_MOVIE,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};
