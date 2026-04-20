# 🏠 Housing-Price-Prediction(End to End ML Project)
built an end-to-end machine learning pipeline to predict housing prices using structured real estate data. The project covers the full lifecycle from data preprocessing and feature engineering to model training, evealuation, and deployment.

To improve model performance, i handled skewed distribution by applying log transformations to key variables like price and area,reducing variance and stabilizing relationships. Categorical features were encoded using one-hot encoding, while careful feature selection was applied to avoid multicollinearity and redundant information.

Multiple models were trained and evaluated, including Linear Regression, Ridge, Lasso, and ensemble methods. RIDGE Regression was selected as the final model due to its balance between performance and generalization, achieving the best correlation of R square (R2) and error metrics.

  The final model was deployed using Streamlit, enabling users to input property features and receive real-time price predictions. Predictions were generated in log scale and converted back to real-world values for interpretability.

## ⚠ Challenges and Solutions
  - Skewness Data Distribution
    The target variable(price) was highly skewed,which negatively impacted model performance.
    -> Solved using log transformation and imporved leanring.
    
  - Multicollinearity Between Features
    Features like area and its log versio created redundancy.
    -> Addressed by removing duplicate representations and using only transformed variables.

  - Categorical Encoding Decisions
    Choosing between label encoding and one-hot encoding required careful consideration.
    -> Implemented one_hot encoding to avoid introducing false ordinal relationships.

  - Model Overfitting VS Generalization
    Complex models like Random Forest underperformed compared to simpler models.
    -> Selected Ridge Regression for better generalization and stability.

  - Deployment Consistency
    Ensuring the Streamlit app used the exact same feature structure as training data.
    -> Solved by saving model and feature columns to maintain consistency.

## 💼 Business Impact
  - Improved Pricing Accuracy
    Helps real estate businesses and agents estimate property values more reliably.
    
  - Faster Decision-Making
    Reduces manual valuation effort, enabling quicker buying,selling or investment decisions.

   - Scalable Solution
     The deployed app allows multiple users to get instant predictions without technical knowledgee.
   
   - Data- Driven Insights
     Highlights key factors influencing house prices(e.g Area, bathrooms, amentites), supporting strategic planning.

   - User-Friendly Tool
    The Streamlit interface transforms a complex ML model into an accessible tool for non-technical users.

## 🛠 Key Highlights
- Built a full ML pipeline from raw data to deployment
- Applied log Transformation  to handle skewness and improve model accuracy
- Performed feature selection using correlation analysis
- Compared multiple models and selected the best-performing one.
- Deployed an interactive web app using Strealit

### Tech Stack 
Python, Pandas,  Numpy, Scikit-learn, Matplotlib, Seaborn, Streamlit

## 📈 Outcome
Developed a reliable regression model capable of predicting housing prices with strong performance while maintaining interpretability and deployment readiness.
    

