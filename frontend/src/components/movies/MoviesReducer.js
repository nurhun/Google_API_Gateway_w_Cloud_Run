import { GET_MOVIES, ADD_MOVIE, UPDATE_MOVIE, DELETE_MOVIE } from "./MoviesTypes";

const initialState = {
  notes: []
};

export const notesReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_MOVIES:
      return {
        ...state,
        notes: action.payload
      };
    case ADD_MOVIE:
      return {
        ...state,
        notes: [...state.notes, action.payload]
      };
    case DELETE_MOVIE:
      return {
        ...state,
        notes: state.notes.filter((item, index) => item.id !== action.payload)
      };
    case UPDATE_MOVIE:
      const updatedNotes = state.notes.map(item => {
        if (item.id === action.payload.id) {
          return { ...item, ...action.payload };
        }
        return item;
      });
      return {
        ...state,
        notes: updatedNotes
      };
    default:
      return state;
  }
};
