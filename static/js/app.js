var app = angular.module('ngoapp',['angular-loading-bar', 'ngAnimate']);

app.controller('NgoController',function($scope,$http){
    $scope.searchparam = "ngoname";
    $scope.searchvalue ="";
    $scope.placeholder="Search by NGO Name";
    $scope.page = 1;
    $scope.page_count = 1;
    $scope.pages=_.range(1,$scope.page_count);


  $scope.changeparam = function(param){
    $scope.searchparam = param;
    $('#searchtype').html(param);
    $scope.searchvalue = "";

    switch (param) {

      case "ngoname":$scope.placeholder="Search by Name of NGO...";
        break;
      case "regno":$scope.placeholder="Search by Registration Number...";
        break;
      case "state":$scope.placeholder="Search by State...";
        break;

      case "city":$scope.placeholder="Search by City...";
        break;
      case "sector":$scope.placeholder="Search by Sectors...";
        break;

      default:
    }
  } ;
  $scope.setpagestart =function(){
    $scope.page = 1;
  };

  $scope.searchngo = function(searchvalue) {
    $http({
  method: 'GET',
  url: '/'+$scope.searchparam+'/'+searchvalue+'?limit=20&page='+$scope.page
}).then(function successCallback(response) {
        $scope.ngos=response.data;
        $scope.page_count = parseInt($scope.ngos[0]._metadata.page_count);
        $scope.pages = _.range(1,$scope.page_count+1);
        $scope.ngos.splice(0,1);

  }, function errorCallback(response) {

  });};



});
