from spark_session import getSparkInstance
from pyspark.ml.linalg import Vectors
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import LinearRegression

spark = getSparkInstance()

ad = spark.read.csv('data/Advertising.csv', header=True, inferSchema=True)
ad.show(5)


lr = LinearRegression(featuresCol = 'features', labelCol = 'label')


ad_df = ad.rdd.map(lambda x: [Vectors.dense(x[0:3]), x[-1]]).toDF(['features', 'label'])
ad_df.show(5)


lr_model = lr.fit(ad_df)

pred = lr_model.transform(ad_df)
pred.show(5)


evaluator = RegressionEvaluator(predictionCol='prediction', labelCol='label')
evaluator.setMetricName('r2').evaluate(pred)

training, test = ad_df.randomSplit([0.8, 0.2], seed=123)

##=====build cross valiation model======

# estimator
lr = LinearRegression(featuresCol='features', labelCol='label')

# parameter grid
from pyspark.ml.tuning import ParamGridBuilder

param_grid = ParamGridBuilder(). \
    addGrid(lr.regParam, [0, 0.5, 1]). \
    addGrid(lr.elasticNetParam, [0, 0.5, 1]). \
    build()

# evaluator
evaluator = RegressionEvaluator(predictionCol='prediction', labelCol='label', metricName='r2')

# cross-validation model
from pyspark.ml.tuning import CrossValidator

cv = CrossValidator(estimator=lr, estimatorParamMaps=param_grid, evaluator=evaluator, numFolds=4)

cv_model = cv.fit(training)

pred_training_cv = cv_model.transform(training)
pred_test_cv = cv_model.transform(test)

pred_training_cv = cv_model.transform(training)
pred_test_cv = cv_model.transform(test)

# performance on test data
evaluator.setMetricName('r2').evaluate(pred_test_cv)


print('Intercept: ', cv_model.bestModel.intercept, "\n",
     'coefficients: ', cv_model.bestModel.coefficients)


print('best regParam: ' + str(cv_model.bestModel._java_obj.getRegParam()) + "\n" +
     'best ElasticNetParam:' + str(cv_model.bestModel._java_obj.getElasticNetParam()))