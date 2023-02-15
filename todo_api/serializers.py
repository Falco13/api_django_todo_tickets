from rest_framework import serializers
from todo_api.models import Todo, Status, Image, Comment


class ImageSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Image
        fields = ['img', 'img_title', 'creator']


class FilterCommentListSerializer(serializers.ListSerializer):
    """Filtering for only parents comments, exclude children"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Recursive children-comments, nested comments"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CreateCommentSerializer(serializers.ModelSerializer):
    """Create comment"""

    class Meta:
        model = Comment
        fields = ['text', 'author', 'children', 'parent']


class CommentSerializer(serializers.ModelSerializer):
    """Detail comment"""
    author = serializers.SerializerMethodField(read_only=True)
    children = RecursiveSerializer(many=True)

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ['id', 'text', 'author', 'created_at', 'children']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['title']


class TodoListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    status = serializers.SlugRelatedField(slug_field='title', queryset=Status.objects.all())
    assigned_to = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)
    image = ImageSerializer(many=True, required=False)
    todo_comments = CommentSerializer(many=True)

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Todo
        fields = ['id', 'title', 'text', 'author', 'status', 'assigned_to', 'created_at', 'updated_at', 'image',
                  'todo_comments']


class TodoCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.SlugRelatedField(slug_field='title', queryset=Status.objects.all())

    class Meta:
        model = Todo
        fields = ['id', 'title', 'text', 'author', 'status', 'assigned_to', 'created_at', 'updated_at', 'image']


class TodoDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    status = serializers.SlugRelatedField(slug_field='title', queryset=Status.objects.all())
    assigned_to = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Todo
        fields = ['id', 'title', 'text', 'author', 'status', 'assigned_to', 'created_at', 'updated_at', 'image']


class UpdateMixin(serializers.ModelSerializer):
    def get_extra_kwargs(self):
        kwargs = super().get_extra_kwargs()
        no_update_fields = getattr(self.Meta, "no_update_fields", None)

        if self.instance and no_update_fields:
            for field in no_update_fields:
                kwargs.setdefault(field, {})
                kwargs[field]["read_only"] = True
        return kwargs


class CheckStatusSerializer(UpdateMixin, serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    status = serializers.SlugRelatedField(slug_field='title', queryset=Status.objects.all())
    assigned_to = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Todo
        fields = '__all__'
        no_update_fields = ['title', 'text', 'author', 'assigned_to', 'created_at', 'updated_at', 'image']
