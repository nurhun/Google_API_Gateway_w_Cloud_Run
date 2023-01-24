import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Button, Form } from "react-bootstrap";
import { addNote } from "./MoviesActions";

class AddNote extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: "",
      year: "",
      description: ""
    };
  }
  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onAddClick = () => {
    const note = {
      title: this.state.title,
      year: this.state.year,
      description: this.state.description
    };
    this.props.addNote(note);
  };

  render() {
    return (
      <div>
        <h2>Add new movie</h2>
        <Form>
          <Form.Group controlId="titleId">
            <Form.Label>Title</Form.Label>
            <Form.Control
              type="text"
              name="title"
              placeholder="Enter movie title"
              value={this.title}
              onChange={this.onChange}
            />
          </Form.Group>
          <Form.Group controlId="yearId">
            <Form.Label>Year</Form.Label>
            <Form.Control
              type = "text"
              name="year"
              placeholder="Enter release year"
              value={this.content}
              onChange={this.onChange}
            />
          </Form.Group>
          <Form.Group controlId="descriptionId">
            <Form.Label>Storyline</Form.Label>
            <Form.Control
              type = "text"
              name="description"
              placeholder="Enter movie description."
              value={this.content}
              onChange={this.onChange}
            />
          </Form.Group>
        </Form>
        <Button variant="success" onClick={this.onAddClick}>
          Add movie
        </Button>
      </div>
    );
  }
}

AddNote.propTypes = {
  addNote: PropTypes.func.isRequired
};

const mapStateToProps = state => ({});

export default connect(mapStateToProps, { addNote })(withRouter(AddNote));
