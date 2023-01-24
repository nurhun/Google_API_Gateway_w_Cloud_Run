import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { deleteNote, updateNote } from "./MoviesActions";
import { Button } from "react-bootstrap";

class Note extends Component {
  onDeleteClick = () => {
    const { note } = this.props;
    this.props.deleteNote(note.id);
  };
  onUpperCaseClick = () => {
    const { note } = this.props;
    this.props.updateNote(note.id, {
      title: note.title.toUpperCase()
    });
  };
  onLowerCaseClick = () => {
    const { note } = this.props;
    this.props.updateNote(note.id, {
      title: note.title.toLowerCase()
    });
  };
  render() {
    const { note } = this.props;
    return (
      <div>
        <hr />
        <p>
           <strong>Title: </strong> {note.title} <br/>
           <strong>Year: </strong> {note.year} <br/>
           <strong>Storyline: </strong> {note.description} <br/>
          {/* (id:{note.id}) {note.title} */}
        </p>
        <Button variant="warning" size="sm" onClick={this.onUpperCaseClick}>
        {/* <Button variant="secondary" size="sm" onClick={this.onUpperCaseClick}> */}
          Upper case
        </Button>{" "}
        <Button variant="dark" size="sm" onClick={this.onLowerCaseClick}>
        {/* <Button variant="info" size="sm" onClick={this.onLowerCaseClick}> */}
          Lower case
        </Button>{" "}
        <Button variant="danger" size="sm" onClick={this.onDeleteClick}>
          Delete
        </Button>
      </div>
    );
  }
}

Note.propTypes = {
  note: PropTypes.object.isRequired
};
const mapStateToProps = state => ({});

export default connect(mapStateToProps, { deleteNote, updateNote })(
  withRouter(Note)
);
