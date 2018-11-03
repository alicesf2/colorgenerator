import React, { Component } from "react";
import {
  Card,
  CardBody,
  CardTitle,
  Container,
  Row,
  Col,
  Button,
  Form,
  FormGroup,
  Label,
  Input
} from "reactstrap";
import "./App.css";

class App extends Component {
  state = {
    login: true,
    search: false,
    display: false
  };

  renderLoginButton = () => {
    return (
      <div className="text-center">
        <Button className="login" outline color="success" size="lg">
          {" "}
          Login to Spotify
        </Button>
      </div>
    );
  };

  renderSearchBar = () => {
    return (
      <Form control>
        <FormGroup className="mb-2 mr-sm-2 mb-sm-0">
          <Label for="searchBar" />
          <Input
            type="text"
            bsSize="lg"
            placeholder="Search for a song..."
            onChange={event => {
              this.setState({ query: event.target.value });
            }}
            value={this.state.query}
            onKeyPress={event => {
              if (event.key === "Enter") {
                event.preventDefault();
                // TODO: handleEnter
              }
            }}
          />
        </FormGroup>
      </Form>
    );
  };

  search = () => {
    console.log("searching");
    if (success) {
      this.searchCallback(result);
    } else {
      console.log(message);
    }
  };

  render() {
    if (this.state.login === true) {
      return (
        <Container fluid={true}>
          <h1 className="header">Color Generator</h1>
          {this.renderLoginButton()}
        </Container>
      );
    }

    if (this.state.search === true) {
      return (
        <Container fluid={true}>
          <h1 className="header">Color Generator</h1>
          {this.renderSearchBar()}
        </Container>
      );
    }

    if (this.state.display === true) {
      return (
        <Container fluid={true}>
          <h1 className="header">Color Generator</h1>
          <Row>
            <Col lg="4">
              <Card className="card">
                <CardTitle>Card 1</CardTitle>
                <CardBody className="color" />
              </Card>
            </Col>
            <Col lg="4">
              <Card className="card">
                <CardTitle>Card 2</CardTitle>
                <CardBody className="color" />
              </Card>
            </Col>
            <Col lg="4">
              <Card className="card">
                <CardTitle>Card 3</CardTitle>
                <CardBody className="color" />
              </Card>
            </Col>
          </Row>
        </Container>
      );
    }
  }
}

export default App;
