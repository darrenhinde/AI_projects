import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col, Card } from 'react-bootstrap';
import { useInView } from 'react-intersection-observer';

// Component to wrap sections for fade-in effect
function FadeInSection(props) {
  const { ref, inView } = useInView({
    triggerOnce: true, // Trigger animation only once
    threshold: 0.1, // Trigger when 10% of the element is in view
  });

  return (
    <div ref={ref} className={`fade-in-section ${inView ? 'is-visible' : ''}`}>
      {props.children}
    </div>
  );
}

function Home() {
  return (
    <Container fluid className="bg-dark text-white" style={{ padding: '20px' }}>
      <style>
      {`
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(20px); }
          to { opacity: 1; transform: translateY(0); }
        }

        .fade-in-section {
          opacity: 0;
          transform: translateY(20px);
          transition: opacity 0.5s ease-out, transform 0.5s ease-out;
        }

        .is-visible {
          opacity: 1;
          transform: translateY(0);
          animation: fadeIn 1s ease-out forwards;
        }

        .background-text {
          font-size: 1.5rem;
          line-height: 2.5;
        }
      `}
      </style>
      <Row className="justify-content-center align-items-start">
        <Col lg={10}>

          <FadeInSection>
            <h1 className="display-3 text-center my-5">Welcome to CryptoVibes</h1>
          </FadeInSection>
          <FadeInSection>
            <div className="background-text my-5">
              <p>
                Welcome to our GenAI Hackathlon project on sentiment analysis on trending crypto trading videos.
              </p>
            </div>
          </FadeInSection>
          <FadeInSection>
            <div className="background-text my-5">
              <p>
                We track the most recent (within 3 days) YouTube videos related to crypto and rank them based on views.
              </p>
            </div>
          </FadeInSection>

          <FadeInSection>
            <div className="background-text my-5">
              <p>
                After that, we measure the Sentiment of each crypto using GPT-4, assessing whether a cryptocurrency's price will increase or decrease.
              </p>
            </div>
          </FadeInSection>

          <FadeInSection>
            <div className="background-text my-5">
              <p>
                This sentiment and view data is stored in our database, linked to each respective cryptocurrency.
              </p>
            </div>
          </FadeInSection>

          <FadeInSection>
            <div className="background-text my-5">
              <p>
                A Weighted Score is calculated (Sentiment Score X Views) to evaluate multiple videos and determine a comprehensive sentiment.
              </p>
            </div>
          </FadeInSection>

          <FadeInSection>
            <div className="background-text my-5 pb-5">
              <p>
                By analyzing discourse volume, we gauge public interest in cryptocurrencies, helping identify which are currently capturing attention.
              </p>
            </div>
          </FadeInSection>
          <FadeInSection>
            <div className="background-text my-5 pb-5">
              <p>
                With this project we are aiming to aid any crypto enthusiasts in their trading journey. We hope you will find this product a useful tool in the future. Happy trading!
              </p>
            </div>
          </FadeInSection>
        </Col>
      </Row>
    </Container>
  );
}

export default Home;
